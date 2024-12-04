#This folder contains Python scripts for data processing and automation.
import boto3  #Aws sdk
import requests


bucket_name = 'covid-data-lake-anthonytony-itoyah'
data_url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'

def upload_to_s3():
    '''Fetch data from url and upload to s3 butcket'''
    
    s3 = boto3.client('s3')

    response = requests.get(data_url)

    if response.status_code == 200:
        s3.put_object(Bucket=bucket_name, Key="raw-data/covid-data.csv", Body=response.content)
        print("Data successfully uploaded")
    else:
        print("f'Upload failed with a {response.status_code} error")

if __name__ == "__main__":
    upload_to_s3()