import pandas as pd
import random

random.seed(42)

careers = {
    "Data Scientist": {
        "interest": "Data Science",
        "work_type": "Data",
        "career_goal": "Job"
    },
    "Machine Learning Engineer": {
        "interest": "Artificial Intelligence",
        "work_type": "Research",
        "career_goal": "Job"
    },
    "Full Stack Developer": {
        "interest": "Web Development",
        "work_type": "Programming",
        "career_goal": "Job"
    },
    "Software Developer": {
        "interest": "Software Development",
        "work_type": "Programming",
        "career_goal": "Job"
    },
    "Cyber Security Analyst": {
        "interest": "Cyber Security",
        "work_type": "Security",
        "career_goal": "Job"
    },
    "Database Administrator": {
        "interest": "Database",
        "work_type": "Data",
        "career_goal": "Job"
    },
    "Network Engineer": {
        "interest": "Networking",
        "work_type": "Networking",
        "career_goal": "Job"
    },
    "Cloud Engineer": {
        "interest": "Cloud Computing",
        "work_type": "Networking",
        "career_goal": "Job"
    },
    "UI UX Designer": {
        "interest": "UI UX",
        "work_type": "Design",
        "career_goal": "Freelancing"
    }
}


rows = []


for career, profile in careers.items():

    for i in range(20):

        overall_percentage = random.randint(65, 95)

        programming_marks = random.randint(60, 95)
        maths_marks = random.randint(55, 95)
        database_marks = random.randint(55, 95)
        os_marks = random.randint(55, 95)
        network_marks = random.randint(55, 95)

        projects_completed = random.randint(1, 8)

        python = random.randint(1, 5)
        java = random.randint(1, 5)
        cpp = random.randint(1, 5)
        html_css = random.randint(1, 5)
        javascript = random.randint(1, 5)
        sql_skill = random.randint(1, 5)
        machine_learning = random.randint(1, 5)
        data_analysis = random.randint(1, 5)
        git = random.randint(1, 5)
        cloud = random.randint(1, 5)

        communication = random.randint(1, 5)
        problem_solving = random.randint(1, 5)
        teamwork = random.randint(1, 5)
        leadership = random.randint(1, 5)
        critical_thinking = random.randint(1, 5)
        creativity = random.randint(1, 5)
        time_management = random.randint(1, 5)

        rows.append({
            "overall_percentage": overall_percentage,
            "programming_marks": programming_marks,
            "maths_marks": maths_marks,
            "database_marks": database_marks,
            "os_marks": os_marks,
            "network_marks": network_marks,
            "projects_completed": projects_completed,

            "python": python,
            "java": java,
            "cpp": cpp,
            "html_css": html_css,
            "javascript": javascript,
            "sql_skill": sql_skill,
            "machine_learning": machine_learning,
            "data_analysis": data_analysis,
            "git": git,
            "cloud": cloud,

            "communication": communication,
            "problem_solving": problem_solving,
            "teamwork": teamwork,
            "leadership": leadership,
            "critical_thinking": critical_thinking,
            "creativity": creativity,
            "time_management": time_management,

            "interest": profile["interest"],
            "work_type": profile["work_type"],
            "career_goal": profile["career_goal"],

            "career": career
        })


df = pd.DataFrame(rows)


df.to_csv(
    "ai/training_data_new.csv",
    index=False
)


print("New training dataset created successfully!")

print("Number of records:", len(df))

print("Number of columns:", len(df.columns))

print("\nCareer distribution:")
print(df["career"].value_counts())

print("\nColumns:")
print(df.columns.tolist())