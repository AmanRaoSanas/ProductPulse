resource "aws_dynamodb_table" "device_metadata" {
  name = var.dynamodb_metadata_table
  billing_mode = "PAY_PER_REQUEST"
  hash_key = "device_id"

  attribute {
    name = "device_id"
    type = "S"
  }

  tags = {
    Project = "ProductPulse"
  }
}

resource "aws_dynamodb_table" "telemetry_cache" {
  name = var.dynamodb_cache_table
  billing_mode = "PAY_PER_REQUEST"
  hash_key = "cache_key"

  attribute {
    name = "cache_key"
    type = "S"
  }

  ttl {
    attribute_name = "ttl_timestamp"
    enabled = true
  }

  tags = {
    Project = "ProductPulse"
  }
}