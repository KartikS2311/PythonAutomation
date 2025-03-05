import pandas as pd
import pytest

df = pd.read_csv('customer.csv')
#1 Null value check(Customer_ID,Name,Email,Country)
def test_NullValueCheck():
    assert df['Customer_id'].notnull().all(),"Null value in Customer_ID"
    assert df['Name'].notnull().all(), "Null value in Name"
    assert df['Email'].notnull().all(), "Null value in Email"
    assert df['Country'].notnull().all(), "Null value in Country"
#2 Duplicate check (Customer_ID)
def test_duplicate_customerid_check():
    duplicated_df =  df[df.duplicated(subset = ['Customer_id'])]
    assert duplicated_df.empty, f"customer_id is having duplicates:\n{duplicated_df}"
# Customer not available from china ( country == china not allowed)
def test_country_china():
    assert df[df['Country'] == 'China'].empty, "China exists"