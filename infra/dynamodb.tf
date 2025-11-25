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