import pandas as pd
from sqlalchemy import create_engine
db_path = r"C:\Users\Kartikay\ETLValidation.db"  # Full database path
engine = create_engine(f"sqlite:///{db_path}")


def load_aggregated_summary_level(table_name):
    df_src = pd.read_excel('transaction_data.xlsx')
    df_aggregated = df_src.groupby('Customer ID')['Total Amount'].sum().reset_index()
    df_aggregated.to_sql(table_name,engine,if_exists='replace',index=False)
    print(f"Data successfully loaded into table '{table_name}'.")

(load_aggregated_summary_level
 ('customer_aggregated_data'))
