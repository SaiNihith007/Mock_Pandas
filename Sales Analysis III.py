import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = sales[(sales['sale_date'] < '2019-01-01') | (sales['sale_date'] > '2019-03-31')]

    df1 = sales[(sales['sale_date'] >= '2019-01-01') & (sales['sale_date'] <= '2019-03-31')]
    
    only_q = df1[~df1['product_id'].isin(df['product_id'])]

    return product[product['product_id'].isin(only_q['product_id'])][['product_id', 'product_name']] 
    