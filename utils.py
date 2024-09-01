from collections import defaultdict as dd

class Subject:
    def __init__(
        self, 
        name,
        code=None,
        weight=0,
        semesters=[],
        elective=[],
        core=[],
        prof_skills=False,
        further_discipline=False
    ):
        self.name = name
        self.code = code
        self.weight = weight
        self.semesters = semesters
        self.elective = elective
        self.core = core
        self.prof_skill = prof_skills
        self.further_discipline = further_discipline

    def __str__(self):
        return self.name

    def set_weight(self, weight):
        self.weight = weight

class Specialisation:
    def __init__(
        self,
        name,
        id_,
        weight=0
    ):
        self.name = name
        self.id = id_
        self.weight = weight
    
    def __str__(self):
        return self.name
    
def print_schedule(model, display_weight=False):
    print("Subject plan:")
    semesters = dd(list)

    for var in model.getVars():
        if var.X:
            if "-" in var.varName:
                # subject
                sem = int(var.varName[-1])
                semesters[sem].append(var)
            else:
                # specialisation
                print(f"\nSpecialisation: {var.varName}\n")

    for semester, subjects in sorted(semesters.items(), key=lambda x: x[0]):
        print(f"Semester {semester+1}:")
        for subject in subjects:
            suffix = f", weight = {subject.obj}" if display_weight else ""
            print(f"{subject.varName.split(" - ")[0]}{suffix}")
        print()