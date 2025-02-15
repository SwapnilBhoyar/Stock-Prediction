'''
@Author: Swapnil Bhoyar
@Date: 2021-09-14
@Last Modified by: Swapnil Bhoyar
@Last Modified time: 2021-09-14
@Title : Program for fetching data from s3 using boto3.
'''
import pandas as pd
import boto3

client = boto3.client("s3")
path = 's3://stockdata-test/google_stock_data.csv'

def fetcher():
    try:
        data = pd.read_csv(path)
        print(data.head())
        return data

    except Exception:
        return print("Error! Unable to fetch the file!")
