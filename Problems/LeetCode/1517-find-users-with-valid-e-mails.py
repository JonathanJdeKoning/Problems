import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    def valid(s):
        if not s.count("@") == 1: return False
        prefix, suffix = s.split("@")
        if not suffix == "leetcode.com": return False
        if not prefix: return False
        if not prefix[0].isalpha(): return False
        for c in prefix:
            if not (c.isalnum() or c in ".-_"): return False
        return True
    return users[users["mail"].apply(valid)]