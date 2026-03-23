import boto3
import os
import glob
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def upload_hpc_data(input_folder, bucket, prefix):
    s3 = boto3.client('s3')
    files = glob.glob(os.path.join(input_folder, "results-*.csv"))
    for local_file in files:
        file_name = os.path.basename(local_file)
        s3_key = os.path.join(prefix, file_name)
        try:
            s3.upload_file(local_file, bucket, s3_key)
            logger.info(f"Uploaded {file_name}")
        except Exception as e:
            logger.error(f"Error: {e}")

if __name__ == "__main__":
    MY_BUCKET = 'ds2002-qec4gc'
    HPC_PATH = f"/scratch/{os.environ.get('USER')}/ds2002-jobruns/text-analysis/"
    upload_hpc_data(HPC_PATH, MY_BUCKET, 'book-analysis/')
