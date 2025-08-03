import boto3
from app.config import settings
import uuid

s3_client = boto3.client(
    "s3",
    aws_access_key_id=settings.aws_access_key_id,
    aws_secret_access_key=settings.aws_secret_access_key,
    region_name=settings.aws_region,
)

def upload_image_to_s3(file_bytes: bytes, filename: str, content_type: str) -> str:
    unique_filename = f"{uuid.uuid4()}_{filename}"

    s3_client.put_object(
        Bucket=settings.aws_bucket_name,
        Key=unique_filename,
        Body=file_bytes,
        ContentType=content_type,
    )

    return (
        f"https://{settings.aws_bucket_name}.s3.{settings.aws_region}.amazonaws.com/"
        f"{unique_filename}"
    )