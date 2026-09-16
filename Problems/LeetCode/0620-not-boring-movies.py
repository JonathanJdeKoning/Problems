import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    cinema = cinema[cinema["description"] != "boring"]
    cinema = cinema[cinema["id"]%2==1]
    return cinema.sort_values("rating", ascending=False)