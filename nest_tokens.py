"""
This module has been updated to use AWS SSM Parameter Store. 
This not only allows for configuration updates but also stores secrets in an encrypted state.
"""
import requests
import json
import boto3
ssm = boto3.client('ssm', region_name="us-east-1")

#Tokens and IDs
google_oauth_id = None
google_refresh_token = None
google_secret = None


def get_nest_token_parameters():
    global google_secret
    google_secret_param = ssm.get_parameters(Names=["nest_secret"], WithDecryption=True)
    google_secret_param = google_secret_param.get("Parameters")
    google_secret = google_secret_param[0].get("Value")
    
    global google_oauth_id
    oauth_id_param = ssm.get_parameters(Names=["nest_oauth_id"])
    oauth_id_param = oauth_id_param.get("Parameters")
    google_oauth_id = oauth_id_param[0].get("Value")
    
    global google_refresh_token
    refresh_token_param = ssm.get_parameters(Names=["nest_refresh_token"], WithDecryption=True)
    refresh_token_param = refresh_token_param.get("Parameters")
    google_refresh_token = refresh_token_param[0].get("Value")
    

def get_access_token():
    #Retrieve token
    get_nest_token_parameters()
    refresh_url = "https://www.googleapis.com/oauth2/v4/token?client_id={}&client_secret={}&refresh_token={}&grant_type=refresh_token".format(google_oauth_id, google_secret, google_refresh_token)
    access_token_json = requests.post(refresh_url)
    access_token_json = access_token_json.json()
    google_access_token = access_token_json.get("access_token")

    if(google_access_token != None):
        return google_access_token
    else:
        raise Exception("Authentication Error")
