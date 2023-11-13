import json
import os
import requests

def lambda_handler(event, context):
    # TODO implement
    json_even = json.loads(event)
    
    payload = {
        'text': f"Issue Created: {json_event['issue']['html_url']}"
    }
    
    slack_url = os.environ.get("SLACK_URL")
    
    response = requests.post(
        slack_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'}
    )
    
    return response.txt