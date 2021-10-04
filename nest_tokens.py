"""This is the quick solution to handling OAuth tokens. Ideally something like this could be handled by AWS KMS. 
		This solution stores a secret token in plaintext which is obviously not ideal or best practice as it exposes a key security component."""

import requests

#tokens and IDs
google_oauth_id = "854305848149-qrd4mep639e8pk6448t101tavnenbgve.apps.googleusercontent.com"
google_refresh_token = "1//0fc_ydCTb5GSgCgYIARAAGA8SNwF-L9IrxyvMMXW0y7_wRFv75HFwAAcSACk1sqYMlYj53qdUnRLcKJqIfWOqRBD0sYG43yIvsBI"
google_secret = "TTSygcDJqeARhtM7T9J9YbIv"
refresh_url = "https://www.googleapis.com/oauth2/v4/token?client_id={}&client_secret={}&refresh_token={}&grant_type=refresh_token".format(google_oauth_id, google_secret, google_refresh_token)

def get_access_token():
	#retrieve token
	access_token_json = requests.post(refresh_url)
	access_token_json = access_token_json.json()
	google_access_token = access_token_json.get("access_token")

	if(google_access_token != None):
		return google_access_token
	else:
		raise Exception("Authentication Error")