#!/usr/bin/env python3
import boto3
import urllib.request
import sys

def download_file(url, local_filename):
    try:
        print(f"Downloading from {url} ...")
        urllib.request.urlretrieve(url, local_filename)
        print(f"Saved file to {local_filename}")
    except Exception as e:
        print("Download failed:", e)
        sys.exit(1)

def upload_to_s3(local_path, bucket_name, s3_key):
    s3_client = boto3.client('s3')
    s3_client.upload_file(local_path, bucket_name, s3_key)
    print(f"Uploaded {local_path} to s3://{bucket_name}/{s3_key}")

def presigned_url(bucket_name, s3_key, expiration=3600):
    s3_client = boto3.client('s3')
    url = s3_client.generate_presigned_url('get_object',
                                           Params={'Bucket': bucket_name, 'Key': s3_key},
                                           ExpiresIn=expiration)
    return url
if __name__ == "__main__":
    # Define variables
    file_url = "https://gist.github.com/nmagee/e43265d988c10a0bde79aabf7f6d97fe#file-download-py"  # Replace with your file URL
    local_file_path = "download.py"
    bucket_name = "ds2002-f25-aye2vx"  # Replace with your S3 bucket name
    s3_key = "download.py"

    # Download the file from the URL
    download_file(file_url, local_file_path)

    # Upload the file to S3
    upload_to_s3(local_file_path, bucket_name, s3_key)

    # Generate a presigned URL
    url = presigned_url(bucket_name, s3_key)
    print(f"Presigned URL: {url}")
