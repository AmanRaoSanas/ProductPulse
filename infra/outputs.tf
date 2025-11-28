output "raw_telemetry_bucket" {
  value       = aws_s3_bucket.telemetry_raw.bucket
  description = "Name of raw S3 bucket"
}

output "device_metadata_table" {
  value       = aws_dynamodb_table.device_metadata.name
  description = "DynamoDB table for metadata"
}

output "lambda_function_arn" {
  value       = aws_lambda_function.telemetry_lambda.arn
  description = "Lambda function ARN"
}

output "telemetry_cache_table" {
  value       = aws_dynamodb_table.telemetry_cache.name
  description = "DynamoDB table for caching telemetry"
}

output "api_gateway_url" {
  value       = aws_apigatewayv2_stage.prod.invoke_url
  description = "HTTP API Gateway URL for FastAPI endpoints"
}
