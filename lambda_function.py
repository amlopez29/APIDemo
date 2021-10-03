
import requests
import json

def lambda_handler(event, context):
	#json responses from APIs
	weatherData = getWeatherFlowData()
	googleData = getGoogleStatus()
	
	#I left the data alone for proper use, but here for presentation I will turn the data into strings to print to a web browser.
	wds = json.dumps(weatherData.json(), indent=4)
	gds = json.dumps(googleData.json(), indent=4)
	
	#returns HTTP response
	return {
    		"statusCode": 200,
    		"statusDescription": "200 OK",
    		"isBase64Encoded": False,
    		"headers": {
        		"Content-Type": "text/html"
    			},
    		"body": "<h1>API Demo</h1> <h2> WeatherFlow Weather Station Data<h2> <p1>{}<p2> <h3>Nest Thermostat Data<h3> <p2>{}<p2>".format(wds, gds)
	}

def getWeatherFlowData():
	#Token, ID, and API URL for WeatherFLow
	wfStationID = "46911"
	wfAccessToken = "ad4e4993-334e-4459-83cf-f4511bdbec28"
	observationURL = "https://swd.weatherflow.com/swd/rest/observations/station/{}?token={}".format(wfStationID, wfAccessToken)

	#API invocation
	oberservations = requests.get(observationURL)

	#returns JSON with station observations
	return oberservations

def getGoogleAuth():
	#tokens and IDs for Nest/Google
	googleOAUTHID = "854305848149-qrd4mep639e8pk6448t101tavnenbgve.apps.googleusercontent.com"
	googleRefresh = "1//0fc_ydCTb5GSgCgYIARAAGA8SNwF-L9IrxyvMMXW0y7_wRFv75HFwAAcSACk1sqYMlYj53qdUnRLcKJqIfWOqRBD0sYG43yIvsBI"
	goat = "TTSygcDJqeARhtM7T9J9YbIv"
	refreshURL = "https://www.googleapis.com/oauth2/v4/token?client_id={}&client_secret={}&refresh_token={}&grant_type=refresh_token".format(googleOAUTHID, goat, googleRefresh)

	#retrieve token
	gatJSON = requests.post(refreshURL)
	gatJSON = gatJSON.json()
	gAccessToken = gatJSON.get("access_token")

	#verify success
	if(gAccessToken != None):
		return gAccessToken
	else:
		raise Exception("Authentication Error")

def getGoogleStatus():
	#retrieve access token
	googleAcessToken = getGoogleAuth()

	#headers with access token for API call
	apiHeaders = {
		'Content-Type': 'application/json',
		'Authorization': 'Bearer {}'.format(googleAcessToken)
	}
	#Device ID and API URL
	deviceID = "AVPHwEu75kYjAEo3iVR5byvOws96tYDC2Lrpaz32Ajs2PS61PRiJGiI3dkw51h3xI89v2pbcOW-xIc6KlZAxt0ztv7NDhw"
	gapiURL = "https://smartdevicemanagement.googleapis.com/v1/enterprises/39831c32-d4d0-4f03-b6ce-80a04045a2ad/devices/{}".format(deviceID)

	#API invocation
	thermoData = requests.get(gapiURL, headers=apiHeaders)

	#returns JSON with Thermostat Data
	return thermoData

