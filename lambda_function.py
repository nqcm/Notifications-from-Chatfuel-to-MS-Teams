import json
import os
import requests

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def send_message(first_name, last_name, id, img):
    
    URL = os.environ['teams_url']
    name = "{} {}".format(first_name, last_name)
    msg_id = "Messenger ID: {}".format(id)
    
    
    PAYLOAD = {
        "@context": "http://schema.org/extensions",
        "@type": "MessageCard",
        "summary": "New live chat notification for MSF bot.",
        "sections": [
            {
            "activityTitle": "New Live Chat Alert",
            "activitySubtitle": "Following person has requested to talk to a human team member."
            },
            {
            "activityTitle": name,
            "activitySubtitle": msg_id,
            "activityImage": img
            }
        ]
    }
    
    headers = {'content-type': 'application/json'}
    
    requests.post(URL, data=json.dumps(PAYLOAD), headers=headers)


def lambda_handler(event, context):
    first_name = event['queryStringParameters']['first_name']
    last_name = event['queryStringParameters']['last_name']
    id = event['queryStringParameters']['messenger_user_id']
    img = event['queryStringParameters']['profile_pic_url']
    send_message(first_name, last_name, id, img)
    logger.info(f'Request sent for {first_name} {last_name}')
    return {
        'statusCode': 200,
    }
