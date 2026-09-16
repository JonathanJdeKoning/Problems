import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    fq = examinations.groupby("student_id").value_counts().to_frame()
    fq.reset_index()
    base = students.merge(subjects, how="cross")
    res = base.merge(fq, on=["student_id", "subject_name"], how="left")
    res["count"] = res["count"].fillna(0)
    res = res.rename(columns={"count":"attended_exams"})
    return res.sort_values(["student_id", "subject_name"])