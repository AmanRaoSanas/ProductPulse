resource "aws_iam_role" "lambda_role" {
  name = "${var.lambda_function_name}-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_policy_attachment" "lambda_basic_execution" {
  name       = "${var.lambda_function_name}-basic-exec"
  roles      = [aws_iam_role.lambda_role.name]
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_policy" "lambda_s3_dynamodb_policy" {
  name = "${var.lambda_function_name}-s3-dynamodb"
  description = "Allow Lambda to access S3 bucket & DynamoDB table"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "S3Access"
        Effect = "Allow"
        Action = [
          "s3:PutObject",
          "s3:GetObject"
        ]
        Resource = "${aws_s3_bucket.telemetry_raw.arn}/*"
      },

      {
        Sid = "DynamoAccess"
        Effect = "Allow"
        Action = [
          "dynamodb:PutItem",
          "dynamodb:UpdateItem",
          "dynamodb:GetItem"
        ]
        Resource = aws_dynamodb_table.device_metadata.arn
      }
    ]
  })
}


resource "aws_iam_policy_attachment" "lambda_s3_dynamodb_attach" {
  name = "${var.lambda_function_name}-attach"
  roles = [aws_iam_role.lambda_role.name]
  policy_arn = aws_iam_policy.lambda_s3_dynamodb_policy.arn
}