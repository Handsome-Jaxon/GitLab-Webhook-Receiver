import json
import os,logging,requests
logger = logging.getLogger()
logger.setLevel(logging.INFO)

url = "https://notify-api.line.me/api/notify"
access_token = 'Input your line notify authentication token'
headers = {'Authorization': 'Bearer ' + access_token}

def lambda_handler(event, context):
    logger.info('## Request')
    logger.info(event)
    logger.info('## Request Body')
    logger.info(event['body'])
    new_data = json.loads(event['body'])
    action      = new_data['object_kind']
    user        = new_data['user_name']
    repository  = new_data['repository']['name']
    commit      = new_data['commits'][0]['message']
    message = "\nAction : %s\nUser : %s\nRepo : %s\nCommit : %s" %(action,user,repository,commit)
    new_payload = {'message':message}
    #print(new_payload)
    r = requests.post(url, headers=headers, params=new_payload,)
    return {
        'statusCode': 200,
    }
    
