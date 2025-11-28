import os
import logging
from dotenv import load_dotenv
import boto3

load_dotenv()

BUCKET_NAME = os.getenv("BUCKET_NAME")
DYNAMODB_METADATA_TABLE = os.getenv("DYNAMODB_METADATA_TABLE")
DYNAMODB_CACHE_TABLE = os.getenv("DYNAMODB_CACHE_TABLE")
AWS_REGION = os.getenv("AWS_REGION") or boto3.session.Session().region_name

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("productpulse")
