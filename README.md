# APIDemo -
This program will retrieve data from both a personal weather station at my home as well as the Nest Thermostat in my home.
Furthermore, this program also checks the air temperature outside and will use that as a guide to change the cooling temperature setting on the thermostat.
This is done by pulling the current air temperature from the observations returned from the weather station. Then it changes the set_cool() temperature on the thermostat
according to the following guide:

Air temperature <= 23.3C : set thermostat to 22.8C.

23.3C < air temperature <= 29.4C : set thermostat to 24.4C.

29.4C < air temperature <= 35C : set thermostat to 25.6C.

air temperature > 35C : set thermostat to 26.7

This roughly aligns with a power saving strategy that uses less AC as the day warms up.

The program is hosted as an AWS Lambda function and is triggered over HTTP through an Application Load Balancer by a user entering the DNS name for the ALB in a web browser.

The URL for which is here:

Removed for now.

This was done so that the program can be hosted in a serverless configuration that can be demonstrated without worrying about dependencies on a local machine.
The page that loads will display the json data resulting from calling the APIs for each device and querying for their current status. The data structure containing this data remains unchanged so that another service that utilizes it can do so easily.

The WeatherFLow Weather Station is a simple device with options only for retrieving data so it was handled simply using just a function.

The Nest Thermostat is a more complex device with an API that has more options for use. The thermostat was handled by creating a python module for Nest devices. In theory more devices could be added to this module to utilize the Nest API by simply adding a class for each device. In this case, the only class defined is the one created for the thermostat. There are more options available than were implemented here. For the thermostat only the get_info() and set_cool() functions were defined as they were all that was needed for the demonstration. More functionality can be introduced by defining more functions to interact with the API. 

