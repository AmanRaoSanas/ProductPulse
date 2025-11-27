import os
import logging
from dotenv import load_dotenv
import boto3

load_dotenv()

BUCKET_NAME = os.getenv("BUCKET_NAME")
AWS_REGION = os.getenv("AWS_REGION") or boto3.session.Session().region_name
MOCK_S3 = os.getenv("MOCK_S3", "True") == "True"  # set true only for local mocking

logging.basicConfig(
    level=logging.INFO,
    format= "%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("productpulse")
