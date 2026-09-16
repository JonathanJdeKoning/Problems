import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby("class").agg("count")
    df = df[df["student"] >= 5].reset_index()
    return df["class"].to_frame()


