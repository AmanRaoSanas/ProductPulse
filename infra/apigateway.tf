resource "aws_apigatewayv2_api" "fastapi_api" {
  name          = "productpulse-api"
  protocol_type = "HTTP"
  target        = aws_lambda_function.telemetry_lambda.arn
}

resource "aws_lambda_permission" "apigw_invoke_lambda" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.telemetry_lambda.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.fastapi_api.execution_arn}/*/*"
}

resource "aws_apigatewayv2_stage" "prod" {
  api_id      = aws_apigatewayv2_api.fastapi_api.id
  name        = "prod"
  auto_deploy = true
}
