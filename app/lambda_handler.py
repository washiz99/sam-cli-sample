import json
import os
import boto3

if os.getenv("AWS_SAM_LOCAL"):
    s3 = boto3.resource('s3', endpoint_url='http://host.docker.internal:4572/')
    config = '../data/' + os.getenv("RING_SETTING_FILE")
else:
    s3 = boto3.client('s3')
    config = '/tmp/' + os.getenv("RING_SETTING_FILE")


def lambda_handler(event, context):

    try:
        # get clickType
        click_type = event['deviceEvent']['buttonClicked']['clickType']
        print("click type:" + click_type)

        # download ring command config file from s3
        config_json = download_config(s3)

        # upload config file to s3
        if click_type == 'SINGLE':
        elif click_type == 'DOUBLE':

        # run registered lambda

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
