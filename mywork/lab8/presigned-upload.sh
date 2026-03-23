#!/bin/bash
# Check for 3 arguments
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <file> <bucket> <expires>"
    exit 1
fi
aws s3 cp "$1" "s3://$2/"
aws s3 presign "s3://$2/$1" --expires-in "$3"
