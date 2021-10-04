
import requests
import json
import nest_devices
import nest_tokens

def lambda_handler(event, context):
    google_access_token = nest_tokens.get_access_token()
    device_id = "AVPHwEu75kYjAEo3iVR5byvOws96tYDC2Lrpaz32Ajs2PS61PRiJGiI3dkw51h3xI89v2pbcOW-xIc6KlZAxt0ztv7NDhw"
    living_room_thermostat = nest_devices.thermostat(device_id, google_access_token)

    weather_data = get_weatherflow_data()
    google_data = get_google_status(living_room_thermostat)

    set_thermostat_temp(weather_data, living_room_thermostat)

    wds = json.dumps(weather_data.json(), indent=4)
    gds = json.dumps(google_data.json(), indent=4)
    
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

def get_weatherflow_data():
    wf_station_id = "46911"
    wf_access_token = "ad4e4993-334e-4459-83cf-f4511bdbec28"
    observation_url = "https://swd.weatherflow.com/swd/rest/observations/station/{}?token={}".format(wf_station_id, wf_access_token)

    oberservations = requests.get(observation_url)
    return oberservations


def get_google_status(thermostat):
    return thermostat.get_info()

def set_thermostat_temp(weather_data, thermostat):
    local_weather_data = weather_data.json()
    oberservations = local_weather_data.get("obs")
    air_temp = oberservations[0].get("air_temperature")
    if air_temp <= 23.3:
        thermostat.set_cool(22.8)
    elif air_temp > 23.3 and air_temp <= 29.4:
        thermostat.set_cool(24.4)
    elif air_temp > 29.4 and air_temp <= 35:
        thermostat.set_cool(25.6)
    elif air_temp > 35:
        thermostat.set_cool(26.7)
