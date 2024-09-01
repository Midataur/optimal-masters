from collections import defaultdict as dd
from gurobipy import GRB
from random import random
from utils import print_schedule, get_name_by_code
import gurobipy as gp
import data

model = gp.Model("Subject Planning")
model.setObjective(gp.LinExpr(), GRB.MAXIMIZE)

# config
# the first sem of your degree
# 1 is sem 1 on an even year
first_sem = 3
# how many subjects per sem
# only 4 sem degrees are currently supported
load = [4, 3, 3, 2]
demo = False

semesters = dd(list)
specs = dd(lambda: {"core": [], "elective": []})
prof_skills = []
further = []

# for demonstration purposes: randomise weights
if demo:
    for subject in data.subjects:
        if subject.weight == 0:
            subject.set_weight(random()*10)

prereqs = []

# Create subject variables
for subject in data.subjects:
    sub_vars = []
    for semester in subject.semesters:
        effective_sem = (semester - first_sem) % len(load)

        var = model.addVar(
            vtype=GRB.BINARY,
            obj=subject.weight,
            name=f"{subject} - Semester {effective_sem}"
        )

        sub_vars.append(var)

        # sort into semester
        semesters[effective_sem].append(var)

        # sort into specialisations
        for spec in subject.core:
            specs[spec]["core"].append(var)
        
        for spec in subject.elective:
            specs[spec]["elective"].append(var)

        # sort into prof skills
        if subject.prof_skill:
            prof_skills.append(var)

        # sort into further discipline
        if subject.further_discipline:
            further.append(var)

        # deal with future prereqs
        for code in subject.prereqs:
            prereq_name = get_name_by_code(data.subjects, code)

            prereqs.append({
                "subject": var,
                "subject_sem": effective_sem,
                "requires": prereq_name
            })

    if len(subject.semesters) > 1:
        # Add "only take the subject once" constraint
        model.addConstr(gp.quicksum(sub_vars) <= 1)

# Add load constraints
model.addConstrs(
    gp.quicksum(subvar for subvar in semesters[sem])
    == allowed
    for sem, allowed in enumerate(load)
)

model.update()

# Add specialisation constraints
spec_vars = []
for spec in data.specialisations:
    spec_var = model.addVar(
        vtype=GRB.BINARY,
        obj=spec.weight,
        name=spec.name
    )

    spec_vars.append(spec_var)

    # need at least 2 cores
    model.addConstr(gp.quicksum(specs[spec.id]["core"]) >= 2*spec_var)

    # need at least 3 electives
    model.addConstr(gp.quicksum(specs[spec.id]["elective"]) >= 3*spec_var)

    # need to do two subjects in a different spec
    other_subjects = set()
    for other_spec, data in specs.items():
        assert(type(other_spec) == str)
        if other_spec != spec.id:
            other_subjects.update(data["core"])
            other_subjects.update(data["elective"])
    
    model.addConstr(gp.quicksum(other_subjects) >= 2*spec_var)

# Must do exactly one specialisation
model.addConstr(gp.quicksum(spec_vars) == 1)

# Add prof skills constraint
model.addConstr(gp.quicksum(prof_skills) >= 1)

# Add further discipline constraint
model.addConstr(gp.quicksum(further) <= 2)

# Add prerequisite constraints
for constraint in prereqs:
    possible = []

    for sem in range(constraint["subject_sem"]):
        required = model.getVarByName(
            f"{constraint["requires"]} - Semester {sem}"
        )

        # subject actually exists in this sem
        if required:
            possible.append(required)
    
    # add constraint
    model.addConstr(gp.quicksum(possible) >= constraint["subject"])

# Optimize model
model.optimize()

print()
print_schedule(model, display_weight=False)