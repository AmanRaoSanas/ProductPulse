variable "aws_region" {
  description = "AWS region for the project"
  type = string
  default = "ap-south-2"
}

variable "raw_bucket" {
  description = "Raw S3 bucket for storing raw data"
  type = string
}

variable "dynamodb_metadata_table" {
  description = "Dynamodb table for storing device metadata"
  type = string
}

variable "lambda_function_name" {
  description = "Lambda function which is handling the FastAPI backend"
  type = string
}

variable "lambda_handler" {
  description = "Lambda function handler"
  type = string
  default = "app.main.handler"
}

variable "lambda_runtime" {
  description = "Runtime environment for lambda"
  type = string
  default = "python3.11"
}

variable "lambda_timeout" {
  default = 60
}

variable "dynamodb_cache_table" {
  description = "DynamoDB table for cache storage"
  type        = string
}
