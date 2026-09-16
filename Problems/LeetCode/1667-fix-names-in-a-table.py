import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    def title(s):
        return s[0].upper() + s[1:].lower()

    users["name"] = users["name"].apply(title)
    return users.sort_values("user_id")