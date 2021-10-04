import requests

#any nest device can be added to this module at a later date.

api_endpoint = "https://smartdevicemanagement.googleapis.com/v1/"
project_id = "39831c32-d4d0-4f03-b6ce-80a04045a2ad"

class thermostat:



    def __init__(self, device_id, access_token):
        self.device_id = device_id
        self.access_token = access_token
        self.info = None
        self.api_headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.access_token)
        }

    def get_info(self):
        get_info_thermostat_api_url = "enterprises/{}/devices/".format(project_id)

        self.info = requests.get(api_endpoint+get_info_thermostat_api_url+self.device_id, headers=self.api_headers)
        return self.info

    def set_cool(self, temp_celcius):
        set_cool_api_url = "enterprises/{}/devices/".format(project_id)
        command = {
            "command" : "sdm.devices.commands.ThermostatTemperatureSetpoint.SetCool",
            "params" : {
                "coolCelsius" : temp_celcius
            }
        }

        requests.post(api_endpoint+set_cool_api_url+self.device_id+":executeCommand", json=command, headers=self.api_headers)


