output "raw_telemetry_bucket" {
  value = aws_s3_bucket.telemetry_raw.bucket
  description = "The name of raw bucket"
}

output "device_metadata_table" {
  value = aws_dynamodb_table.device_metadata.name
  description = "Dynamodb table for storing device metadata"
}

output "lambda_function_arn" {
  value = aws_lambda_function.telemetry_lambda.arn
}