'''
@Author: Swapnil Bhoyar
@Date: 2021-09-14
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-09-14
@Title : Program for cleaning the data.
'''
import fetchFile

print("\nFetching file from AWS Bucket:")
df = fetchFile.fetcher()

try:
    del df['Adj Close']
    print("\nConverting columns to list:")
    print(df.columns.tolist())

    df = df.rename(columns={df.columns[1]: 'Open'})
    df = df.rename(columns={df.columns[2]: 'High'})
    df = df.rename(columns={df.columns[3]: 'Low'})
    df = df.rename(columns={df.columns[4]: 'Close'})

    print(df.head())

    print("\nChecking the data types:")
    print(df.dtypes)

    print("\nChecking for null values:")
    print(df.isnull().sum())

except Exception:
    print("Error! Something went wrong!")