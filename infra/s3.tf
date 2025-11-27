resource "aws_s3_bucket" "telemetry_raw" {
  bucket = var.raw_bucket

  tags = {
    Project = "ProductPulse"
  }
}

resource "aws_s3_bucket_versioning" "telemetry_raw_versioning" {
  bucket = aws_s3_bucket.telemetry_raw.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_lifecycle_configuration" "telemetry_raw_lifecycle" {
  bucket = aws_s3_bucket.telemetry_raw.id
  rule {
    id     = "remove-old-versions"
    status = "Enabled"

    filter {}

    noncurrent_version_expiration {
      noncurrent_days = 90
    }
  }
}