import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    fq = my_numbers.value_counts().to_frame().reset_index()
    fq = fq[fq["count"] == 1].drop("count", axis=1)
    res = fq[fq["num"]>=fq["num"].max()]

    if len(res) == 0:
        return pd.DataFrame(data={"num": [None]})
    else:
        return res