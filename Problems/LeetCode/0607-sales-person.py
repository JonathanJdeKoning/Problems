import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    so = sales_person.merge(orders, on='sales_id')
    soc = so.merge(company, on='com_id')
    s_red = soc.loc[soc.name_y == 'RED', 'name_x']
    return sales_person.loc[~sales_person.name.isin(s_red), ['name']]
