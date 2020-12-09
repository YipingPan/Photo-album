def lambda_handler(event, context):
    print("LF1 run successfully")
    print("I've updated LF1")
    print("I've updated LF1 again")
    return {
        'statusCode': 200,
    }
