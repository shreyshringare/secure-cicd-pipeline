def lambda_handler(event, context):

    password = "12345"   # Vulnerability for Bandit scan

    return {
        'statusCode': 200,
        'body': 'Hello from Secure CI/CD Pipeline!'
    }
