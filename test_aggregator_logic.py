import pandas as pd
from sqlalchemy import create_engine
engine = create_engine("sqlite:///C:/Users/Kartikay/ETLValidation.db")

def test_sales_data_aggregation_logic():
    df_source = pd.read_csv('sales.csv')
    df_source['Total_Sales_Amount'] = df_source['Price'] * df_source['Quantity']
    expected_df = df_source.groupby('CustomerID')['Total_Sales_Amount'].sum().reset_index()
    print(expected_df)
    actual_df = pd.read_sql("Select * from Total_Sales_Per_Customer",engine)
    print(actual_df)
    assert actual_df.equals(expected_df),"ETL process is not correct"
    print("My test_sales_data_aggregation_logic is passed")
    # if expected_df.equals(actual_df):
    #     print("Test Passed ✅: Data matches the expected aggregation.")
    # else:
    #     print("Test Failed ❌: Data does not match the expected aggregation.")

test_sales_data_aggregation_logic()