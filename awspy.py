#This is a sample proj for AWS py
import boto3

#Let's use Amazon S3
s3 = boto3.resource('s3')

#Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

#Upload a new file
data = open('test.txt','rb')
s3.Bucket('plex-ccp-2021-demo').put_object(Key='test.txt', Body=data)

for bucket in s3.buckets.all():
    print(bucket.name)

