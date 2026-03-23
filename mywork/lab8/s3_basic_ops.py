import boto3
s3 = boto3.client('s3', region_name='us-east-1')
bucket_name = 'ds2002-qec4gc'

def run_tasks():
    # Private upload
    s3.upload_file('uva-logo.jpg', bucket_name, 'private-python.jpg')
    # Public upload
    s3.upload_file('uva-logo.jpg', bucket_name, 'public-python.jpg', 
                   ExtraArgs={'ACL': 'public-read'})
    # Presign
    url = s3.generate_presigned_url('get_object', 
        Params={'Bucket': bucket_name, 'Key': 'private-python.jpg'}, ExpiresIn=3600)
    print(f"Presigned URL: {url}")

if __name__ == "__main__":
    run_tasks()
