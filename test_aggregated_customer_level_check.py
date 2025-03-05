import pandas as pd
import pytest
from sqlalchemy import create_engine
engine = create_engine("sqlite:///C:/Users/Kartikay/ETLValidation.db")

def test_aggregated_summary_level():
#1 extract data from file
    df_src = pd.read_excel('transaction_data.xlsx')
#2 transform data to aggregated level
    df_aggregated = df_src.groupby('Customer ID')['Total Amount'].sum().reset_index()
#3 extract data from target
    df_tgt = pd.read_sql('Select * from customer_aggregated_data',engine)
#4 compare both the dataframes
    assert df_tgt.equals(df_aggregated),"my test failed"
