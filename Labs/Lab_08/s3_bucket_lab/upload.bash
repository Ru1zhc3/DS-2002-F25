#!/bin/bash

set -e

# This script uploads a file to an S3 bucket.
# Usage: ./upload.bash <file_path> <bucket_name>

read -r -p "Enter the file name to upload: " FILE_NAME
read -r -p "Enter the S3 bucket name: " BUCKET
read -r -p "Enter the expiration time in seconds for the pre-signed URL (default 604800 for 7 days): " EXPIRATION
EXPIRATION=${EXPIRATION:-604800}

echo "Uploading $FILE_NAME to s3://$BUCKET/$FILE_NAME ..."
aws s3 cp "$FILE_NAME" "s3://$BUCKET/$FILE_NAME"

echo "Generating pre-signed URL for $FILE_NAME ..."
URL=$(aws s3 presign "s3://$BUCKET/$FILE_NAME" --expires-in "$EXPIRATION")
echo "Presigned URL:"
echo "$URL"
