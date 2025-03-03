import pandas as pd
from sqlalchemy import create_engine
db_path = r"C:\Users\Kartikay\ETLValidation.db"  # Full database path
engine = create_engine(f"sqlite:///{db_path}")

def load_Aggregated_sales_Data_from_CSV(file_path,table_name):
    df = pd.read_csv(file_path)
    df['Total_Sales_Amount'] = df['Price']*df['Quantity']
    grouped_df = df.groupby('CustomerID')['Total_Sales_Amount'].sum().reset_index()
    grouped_df.to_sql(table_name,engine,if_exists='replace',index=False)
    print(f"Data successfully loaded into table '{table_name}'.")

load_Aggregated_sales_Data_from_CSV('sales.csv','Total_Sales_Per_Customer')


