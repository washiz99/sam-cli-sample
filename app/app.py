import json
import os
import boto3

from ring_command import RingCommand


S3_BUCKET = 'soracom-labo-ringcommand'
RING_COMMAND_CONFIG = 'ring-command.json'


if os.getenv("AWS_SAM_LOCAL"):
    s3_client = boto3.resource('s3', endpoint_url='http://host.docker.internal:4572/')
    # lambda_client = boto3.resource('lambda', endpoint_url='http://host.docker.internal:4574/')
else:
    s3_client = boto3.client('s3')
    # lambda_client = boto3.client('lambda')


def lambda_handler(event, context):

    try:
        # get clickType
        click_type = event['deviceEvent']['buttonClicked']['clickType']
        print("  click: " + click_type)

        # download ring command config file from s3
        config_json = download_config(s3_client)

        # click event
        ring = RingCommand(config_json)
        if click_type == 'SINGLE':
            res = ring.turn_next()
            print('  status: ' + str(res))
            print('  lambda: ' + ring.get_command())
        elif click_type == 'DOUBLE':
            res = ring.turn_prev()
            print('  status: ' + str(res))
            print('  lambda: ' + ring.get_command())
        elif click_type == 'LONG':
            print("  Invoke lambda!!")
            """
            lambda_client.invoke(
                FunctionName=ring.get_command(),
                InvocationType="RequestResponse",
                Payload=json.dumps({})
            )
            """

        # upload ring command config file to s3
        upload_config(s3_client, ring.to_json())

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Normal end.",
            }),
        }

    except Exception as e:
        print(e)
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Error occured.",
            }),
        }


def download_config(s3_client):
    s3_client.Bucket(S3_BUCKET).download_file(RING_COMMAND_CONFIG, '/tmp/' + RING_COMMAND_CONFIG)
    with open('/tmp/' + RING_COMMAND_CONFIG, 'r') as f:
        config_json = json.load(f)
    return config_json


def upload_config(s3_client, config_json):
    with open('/tmp/' + RING_COMMAND_CONFIG, 'w') as f:
        json.dump(config_json, f)
    s3_client.Bucket(S3_BUCKET).upload_file('/tmp/' + RING_COMMAND_CONFIG, RING_COMMAND_CONFIG)
    return 0
