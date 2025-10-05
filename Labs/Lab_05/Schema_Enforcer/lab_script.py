import csv
data = [
    ["student_id", "Major", "GPA", "is_cs_major", "credits_taken"],
    [1, "Computer Science", 4.0, "Yes", '20'],
    [2, "English", 3.2, "No", '18'],
    [3, "Mechanical Engineering", 3, "No", "22.5"],
    [4, "Biology", 3.6, "No", '66.5'],
    [5, "Bussiness", 4, "No", '12'],
    [6, "Math", 3.8, "No", '30'],
]
with open("Labs/Lab_05/Schema_Enforcer/raw_survey_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

import json
courses = [
    {
        "course_id": "DS2002",
        "section": "001",
        "title": "Data Science Systems",
        "level": 200,
        "instructors": [
            {"name": "Austin Rivera", "role": "Primary"},
            {"name": "Heywood Williams-Tracy", "role": "TA"}
        ]
    },
    {
        "course_id": "CS4501",
        "section": "001",
        "title": "Autonomous Racing",
        "level": 300,
        "instructors": [
            {"name": "Madhur Behl", "role": "Primary"}
        ]
    },
    {
        "course_id": "CS3100",
        "section": "002",
        "title": "Data Structures and Algorithms II",
        "level": 300,
        "instructors": [
            {"name": "Raymond Pettie", "role": "Primary"}
        ]
    },
    {
        "course_id": "CS3140",
        "section": "001",
        "title": "Software Engineering Essentials",
        "level": 300,
        "instructors": [
            {"name": "Rich Nygn", "role": "Primary"}
        ]
    },
    {
        "course_id": "CS3130",
        "section": "001",
        "title": "Computer Organization II",
        "level": 300,
        "instructors": [
            {"name": "Charles Reeis", "role": "Primary"}
        ]
    }
]
with open("Labs/Lab_05/Schema_Enforcer/raw_course_catalog.json", "w") as f:
    json.dump(courses, f, indent=2)

import pandas as pd
df = pd.read_csv("Labs/Lab_05/Schema_Enforcer/raw_survey_data.csv")
def to_bool(value):
    if isinstance(value, str):
        return value.strip().lower() == "yes"
    return False
df["is_cs_major"] = df["is_cs_major"].apply(to_bool)
df = df.astype({
    "credits_taken": "float64",
    "GPA": "float64"
})
df.to_csv("Labs/Lab_05/Schema_Enforcer/clean_survey_data.csv", index=False)

with open("Labs/Lab_05/Schema_Enforcer/raw_course_catalog.json", "r") as f:
    json_data = json.load(f)
df = pd.json_normalize(
    json_data,
    record_path=['instructors'],
    meta=["course_id", "section", "title", "level"]
)
df.to_csv("Labs/Lab_05/Schema_Enforcer/clean_course_catalog.csv", index=False)
