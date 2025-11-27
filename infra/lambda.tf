resource "aws_lambda_function" "telemetry_lambda" {
  function_name = var.lambda_function_name
  role = aws_iam_role.lambda_role.arn

  handler = var.lambda_handler
  runtime = var.lambda_runtime
  timeout = var.lambda_timeout

  filename         = "${path.module}/lambda_package.zip"
  source_code_hash = filebase64sha256("${path.module}/lambda_package.zip")

  environment {
    variables = {
      BUCKET_NAME = var.raw_bucket
      DYNAMODB_TABLE = var.dynamodb_metadata_table
    }
  }
}