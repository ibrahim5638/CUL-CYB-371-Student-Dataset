import pandas as pd

# Creating a fictional student dataset
data = {
    "Student_ID": ["CUL001", "CUL002", "CUL003", "CUL004", "CUL005",
                   "CUL006", "CUL007", "CUL008", "CUL009", "CUL010"],
    "Department": ["Computer Science", "Cyber Security", "Computer Science",
                  "Software Engineering", "Cyber Security", "Computer Science",
                  "Software Engineering", "Cyber Security", "Computer Science",
                  "Software Engineering"],
    "Level": [100, 200, 300, 100, 200, 300, 400, 100, 200, 400],
    "Attendance_Percentage": [85, 90, 78, 95, 82, 88, 75, 92, 80, 87],
    "Average_Exam_Score": [76, 84, 69, 91, 73, 80, 65, 88, 72, 86]
}

df = pd.DataFrame(data)
print(df)
df.to_csv("student_dataset.csv", index=False)
print("\nDataset successfully created!")
