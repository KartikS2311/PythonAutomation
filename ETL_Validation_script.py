import pandas as pd
source = pd.read_csv('Employee.csv')
print("Test Case 1: Following are the column names in the source file : \n")
print(source.columns)
print("\n")
print("Test Case 2: Rows X Columns in the source file : \n")
print(source.shape)
print("\n")
print("Test Case 3: N of rows under each columns : \n")
print(source.count())
print("\n")

print("Test Case 4: Duplicate records in the source file : \n")
print(source.duplicated().sum())
print("\n")

print("Test Case 5: Duplicate records saved in the file below : \n")
dupes = source[source.duplicated()].to_csv("duplicated.csv")
print("\n")

print("Test Case 6: Check if null exist in dept_name col : \n")
print(source[source['Dept_name'].isnull()])
print("\n")

print("Test Case 7: Unique value of emp_no co n the source : \n")
print(source['emp no'].unique())
print("\n")

print("Test Case 8: Unique value of emp_name co n the source : \n")
print(source['emp_name'].unique())
print("\n")

print("Test Case 9: Unique value of Dept_name co n the source : \n")
print(source['Dept_name'].unique())
print("\n")

print("Test Case 10: Unique value of Salary co n the source : \n")
print(source['Salary'].unique())
print("\n")

print("Test Case 11: Sample top 5 records from source file : \n")
print(source.head())
print("TEST COMPLETED.....\n")

print("Test Case 11: Sample bottom 5 records from source file : \n")
print(source.tail())
print("TEST COMPLETED.....\n")



