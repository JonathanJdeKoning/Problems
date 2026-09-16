import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary["sex"] = salary["sex"].apply(lambda x: "m" if x=="f" else "f")
    return salary