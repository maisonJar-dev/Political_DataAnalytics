import pandas as pd
import io
import csv

import boto3
from boto3.s3.transfer import S3UploadFailedError
from botocore.exceptions import ClientError

class S3Actions:
    def get(self):
        """
        Get the object
        """
        s3 = boto3.client(
            's3',
            aws_access_key_id='AKIATTX4CQ5J2GXHVDCI',
            aws_secret_access_key='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',
            region_name='us-east-2'
        )
        # response = s3.list_objects_v2(Bucket='politcal-eda')
        # print("Files in bucket:")
        # for obj in response.get('Contents', []):
        #     print(obj['Key'])

        obj = s3.get_object(Bucket='politcal-eda', Key='Data/V_Dem_Full.csv')
        df = pd.read_csv(obj['Body'], nrows=5)
    
        print("Column names and types:")
        print(df.dtypes)

if __name__ == "__main__":
    action = S3Actions()
    action.get()