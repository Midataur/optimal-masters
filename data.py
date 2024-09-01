from utils import Subject, Specialisation

specialisations = [
    Specialisation(
        "Applied Mathematics",
        "app"
    ),
    Specialisation(
        "Mathematical Physics",
        "mp"
    ),
    Specialisation(
        "Operations Research",
        "opp"
    ),
    Specialisation(
        "Pure Mathematics",
        "pure"
    ),
    Specialisation(
        "Stats and Stochastics",
        "stat"
    )
]

# Semester 1 is Sem 1 in an even year
# This comes from the masters guide at time of writing
subjects = [
    Subject(
        "Advanced Methods: Transforms",
        code="MAST90067",
        weight=2,
        semesters=[1],
        core=["app", "mp"]
    ),
    Subject(
        "Computational Differential Equations",
        code="MAST90026",
        weight=2,
        semesters=[1],
        elective=["app"]
    ),
    Subject(
        "Random Matrix Theory",
        code="MAST90103",
        weight=2,
        semesters=[1],
        elective=["app", "mp"]
    ),
    Subject(
        "Advanced Biological Modelling: Dynamics",
        code="MAST90127",
        weight=1,
        semesters=[1],
        elective=["app"]
    ),
    Subject(
        "Bayesian Statistical Learning",
        weight=2,
        code="MAST90125",
        semesters=[2, 4],
        elective=["app", "stat"]
    ),
    Subject(
        "Mathematical Biology",
        weight=2,
        code="MAST90011",
        semesters=[2],
        elective=["app"]
    ),
    Subject(
        "Advanced Methods: Differential Equations",
        weight=1.5,
        code="MAST90064",
        semesters=[3],
        core=["app"],
        elective=["mp"]
    ),
    Subject(
        "Mathematical Statistical Mechanics",
        weight=2,
        code="MAST90060",
        semesters=[3],
        core=["mp"],
        elective=["app"]
    ),
    Subject(
        "Continuum Mechanics",
        weight=1,
        code="MAST90113",
        semesters=[4],
        elective=["app"]
    ),
    Subject(
        "Infectious Disease Dynamics",
        weight=1.5,
        code="MAST90129",
        semesters=[4],
        elective=["app"]
    ),
    Subject(
        "Enumerative Combinatorics",
        code="MAST90031",
        semesters=[2],
        elective=["mp"]
    ),
    Subject(
        "Introduction to String Theory",
        code="MAST90069",
        semesters=[2],
        elective=["mp"]
    ),
    Subject(
        "Lie Algebras",
        weight=2,
        code="MAST90132",
        semesters=[3],
        elective=["mp", "pure"]
    ),
    Subject(
        "Advanced Discrete Mathematics",
        code="MAST90030",
        semesters=[4],
        core=["mp"]
    ),
    Subject(
        "Exactly Solveable Models",
        weight=2,
        code="MAST90065",
        semesters=[4],
        elective=["mp"]
    ),
    Subject(
        "Optimisation for Industry",
        code="MAST90014",
        semesters=[1],
        core=["opp"]
    ),
    Subject(
        "Advanced Nonlinear Programming",
        code="MAST90142",
        semesters=[1],
        core=["opp"]
    ),
    Subject(
        "Stochastic Optimisation",
        weight=3,
        code="MAST90144",
        semesters=[1],
        elective=["opp"]
    ),
    Subject(
        "Approximation, Algorithms & Heuristics",
        code="MAST90098",
        semesters=[2, 4],
        core=["opp"],
    ),
    Subject(
        "Network Optimisation",
        code="MAST90013",
        semesters=[2],
        elective=["opp"]
    ),
    Subject(
        "Optimisation for Industry",
        code="MAST90014",
        semesters=[3],
        core=["opp"]
    ),
    Subject(
        "Mathematical Game Theory",
        code="MAST90137",
        semesters=[3],
        elective=["opp"]
    ),
    Subject(
        "Scheduling and Optimisation",
        code="MAST90050",
        semesters=[4],
        elective=["opp"]
    ),
    Subject(
        "Algebraic Topology",
        weight=2,
        code="MAST90023",
        semesters=[1],
        core=["pure"]
    ),
    Subject(
        "Functional Analysis",
        weight=1,
        code="MAST90020",
        semesters=[1],
        elective=["pure"]
    ),
    Subject(
        "Algebraic Number Theory",
        code="MAST90136",
        semesters=[1],
        elective=["pure"]
    ),
    Subject(
        "Groups, Categories, and Homological Algebra",
        code="MAST90068",
        semesters=[2],
        elective=["pure"],
    ),
    Subject(
        "Algebraic Geometry",
        code="MAST90097",
        semesters=[2],
        elective=["pure"]
    ),
    Subject(
        "Differential Geometry",
        weight=2,
        code="MAST90143",
        semesters=[2],
        elective=["pure"]
    ),
    Subject(
        "Measure Theory",
        weight=3,
        code="MAST90012",
        semesters=[3],
        core=["pure"]
    ),
    Subject(
        "Differential Topology",
        code="MAST90029",
        semesters=[3],
        elective=["pure"]
    ),
    Subject(
        "Representation Theory",
        weight=1,
        code="MAST90017",
        semesters=[4],
        elective=["pure"]
    ),
    Subject(
        "Riemann Surfaces & Complex Analysis",
        weight=2,
        code="MAST90056",
        semesters=[4],
        elective=["pure"]
    ),
    Subject(
        "Partial Differential Equations",
        weight=2,
        code="MAST90133",
        semesters=[4],
        elective=["pure"]
    ),
    Subject(
        "Mathematical Statistics",
        weight=1,
        code="MAST90082",
        semesters=[1, 3],
        core=["stat"]
    ),
    Subject(
        "Random Processes",
        weight=2,
        code="MAST90019",
        #semesters=[1, 3],
        # TODO: FIX THIS HACK BY IMPLEMENTING ACTUAL PREREQS
        semesters=[1],
        elective=["stat"]
    ),
    Subject(
        "Statistical Modelling",
        code="MAST90084",
        semesters=[1, 3],
        elective=["stat"]
    ),
    Subject(
        "Inference for Spatial-temporal Processes",
        code="MAST90122",
        semesters=[1, 3],
        elective=["stat"]
    ),
    Subject(
        "Advanced Topics in Stochastic Models",
        weight=1,
        code="MAST90112",
        semesters=[1],
        elective=["stat"]
    ),
    Subject(
        "Advanced Probability",
        weight=3,
        code="MAST90081",
        semesters=[2, 4],
        core=["stat"]
    ),
    Subject(
        "Computational Statistics and Data Science",
        code="MAST90083",
        semesters=[2, 4],
        elective=["stat"]
    ),
    Subject(
        "Multivariate Statistics for Data Science",
        code="MAST90138",
        semesters=[2, 4],
        elective=["stat"]
    ),
    Subject(
        "Practice of Statistics and Data Science",
        code="MAST90027",
        semesters=[2],
        elective=["stat"]
    ),
    Subject(
        "Mathematics of Risk",
        code="MAST90051",
        semesters=[2],
        elective=["stat"]
    ),
    Subject(
        "Advanced Statistical Modelling",
        code="MAST90111",
        semesters=[2],
        elective=["stat"]
    ),
    Subject(
        "Stochastic Calculus with Applications",
        weight=2,
        code="MAST90059",
        semesters=[3],
        elective=["stat"]
    ),
    # Can't tell if this is available anymore
    Subject(
        "Experimental Mathematics",
        code="MAST90053",
        weight=-10**6
    ),
    Subject(
        "The Art of Scientific Computation",
        code="COMP90072",
        semesters=[1, 2, 3, 4],
        prof_skills=True
    ),
    Subject(
        "Systems Modelling and Simulation",
        code="MAST90045",
        semesters=[3],
        prof_skills=True
    ),
    Subject(
        "Ethics and Responsiblity in Science",
        weight=1,
        code="SCIE90005",
        semesters=[1, 3],
        prof_skills=True
    ),
    Subject(
        "Scientific Communication",
        weight=2,
        code="SCIE90012",
        semesters=[2, 4],
        prof_skills=True
    ),
    Subject(
        "Communication for Research Scientists",
        weight=1,
        code="SCIE90013",
        semesters=[1, 2, 3, 4],
        prof_skills=True
    ),
    Subject(
        "Science and Technology Internship",
        code="SCIE90017",
        semesters=[1, 2, 3, 4],
        prof_skills=True
    ),
    Subject(
        "Introduction to Quantum Computing",
        weight=1,
        code="MULT90063",
        semesters=[1, 3],
        prof_skills=True
    ),
    # ???
    # handbook page just says "available in july"
    # idk what that means lmao
    Subject(
        "Science and AI: Legal & Ethical Challenges",
        code="LAWS90203",
        weight=-10**6,
        prof_skills=True
    ),
    Subject(
        "Critical Communication for Engineers",
        code="ENGR90021",
        semesters=[1, 2, 3, 4],
        prof_skills=True
    ),
    Subject(
        "Quantum Mechanics",
        code="PHYC90007",
        semesters=[1, 3],
        further_discipline=True
    ),
    Subject(
        "Quantum Field Theory",
        code="PHYC90008",
        semesters=[1, 3],
        further_discipline=True
    ),
    Subject(
        "Physical Cosmology",
        code="PHYC90009",
        semesters=[1],
        further_discipline=True
    ),
    Subject(
        "Statistical Mechanics",
        code="PHYC90010",
        semesters=[1, 3],
        further_discipline=True
    ),
    Subject(
        "Particle Physics",
        code="PHYC90011",
        semesters=[2, 4],
        further_discipline=True
    ),
    Subject(
        "General Relativity",
        code="PHYC90012",
        semesters=[2, 4],
        further_discipline=True
    ),
    Subject(
        "Algorithms and Complexity",
        code="COMP90038",
        semesters=[1, 2, 3, 4],
        further_discipline=True
    ),
    Subject(
        "Cryptography and Security",
        code="COMP90043",
        semesters=[2, 4],
        further_discipline=True
    ),
    # I don't think this is running atm
    Subject(
        "Constraint Programming",
        code="COMP90046",
        weight=-10**6,
        further_discipline=True
    ),
    Subject(
        "Declarative Programming",
        code="COMP90048",
        semesters=[1, 3],
        further_discipline=True
    ),
    Subject(
        "Introduction to Machine Learning",
        code="COMP90049",
        semesters=[1, 2, 3, 4],
        further_discipline=True
    ),
    Subject(
        "Statistical Machine Learning",
        weight=1,
        code="COMP90051",
        semesters=[1, 2, 3, 4],
        further_discipline=True
    ),
    Subject(
        "Introduction to Programming",
        code="COMP90059",
        semesters=[1, 2, 3, 4],
        further_discipline=True
    ),
    Subject(
        "Statistics for Bioinformatics",
        code="BINF90001",
        semesters=[1, 3],
        further_discipline=True
    ),
    Subject(
        "Elements of Bioinformatics",
        code="BINF90002",
        semesters=[1, 3],
        further_discipline=True
    ),
    Subject(
        "Systems and Synthetic Biology",
        code="BMEN90027",
        semesters=[3],
        further_discipline=True
    )
]