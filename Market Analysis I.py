import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders_2019 = orders[(orders['order_date'] >= '2019-01-01') & (orders['order_date'] <= '2019-12-31')]
    orders_count = orders_2019.groupby(['buyer_id']).order_id.count().reset_index()
    print(orders_count)
    df = users.merge(orders_count, how = 'left',left_on = 'user_id', right_on = 'buyer_id')
    print(df)
    df['order_id'] = df['order_id'].fillna(0)
    print(df)
    return df[['user_id','join_date','order_id']].rename(columns={'user_id':'buyer_id','order_id':'orders_in_2019'})
    