import pytest
import pandas as pd

#test if there are any duplicate records/rows in target system
def test_checkDuplicates():
    target_df = pd.read_csv("target.csv",sep=",")
    count = target_df.duplicated().sum()
    assert count == 0 , "Duplicates found - please verify target"

#test if target is not blank
def test_DataCompleteness():
    target_df = pd.read_csv("target.csv",sep=",")
    assert not target_df.empty,"Target file is empty- please verify ETL process"

#test if deptno is a mandatory column
def test_deptNpFprNullValueCheck():
    target_df = pd.read_csv("target.csv", sep=",")
    isDeptNoNull = target_df['deptno'].isnull().any()
    assert isDeptNoNull == False , "deptno is having null- Please check"

#test if eno is always a primary key
def test_enoNoForUniqueValueCheck():
    target_df = pd.read_csv("target.csv", sep=",")
    totalcount = target_df['eno'].count()
    deptNoUniqueValueCount = len(target_df['eno'].unique())
    assert totalcount == deptNoUniqueValueCount, "eno column values are not unique"



