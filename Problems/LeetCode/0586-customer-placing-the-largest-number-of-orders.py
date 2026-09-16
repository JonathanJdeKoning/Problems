import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return orders.mode().head(1)["customer_number"].to_frame()
