import boto3

#Initialize the s3 client
s3 = boto3.client('s3')

# # List all the buckets
response = s3.list_buckets()
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

bucket_name = "dhruv-first-bucket"
file_key = "requirements.txt"

s3.download_file(bucket_name, file_key, file_key + "_downloaded")

#Read and print the content of the file
with open(file_key + "_downloaded", "r") as file:
    print(file.read())