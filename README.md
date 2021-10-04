# APIDemo
API Demo program

This program will retrieve data from both a personal weather station at my home as well as the Nest Thermostat in my home.
Furthermore, this program also checks the air temperature outside and will use that as a guide to change the cooling temperature setting on the thermostat.
The program is hosted as a AWS Lambda function and is triggered over HTTP through an Application Load Balancer by a user entering the DNS name for the ALB in a web browser.
The URL for which is here:
APIDemo-alb-1492775925.us-east-1.elb.amazonaws.com

This was done so that the program can be hosted in a serverless configuration that can be demonstrated without worrying about dependencies on a local machine.
The page that loads will display the json data resulting from calling the APIs for each device and querying for their current status.

