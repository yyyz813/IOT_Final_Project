#########################################################
#          Cleaning and Normalizing Script              #
#########################################################
# Import Libraries
import requests
import jinja2
import ast
import json
from Tools.scripts.dutree import display
from pandas.io.json import json_normalize
import pandas as pd

# Set the table size for view
pd.set_option('display.width',1000)
pd.set_option('display.max_row',500)
pd.set_option('display.max_columns',500)

# Header for the request
headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJfaWQiOiI1NjUzODUyNjAyNzYxMjE2IiwiZmlyc3ROYW1lIjoiUENDSSIsImxhc3ROYW1lIjoiVGVzdCIsImVtYWlsIjoiZGV2ZWxvcGVyc19uYW5vQHBjY2lubm92YXRpb24ub3JnIiwiaWF0IjoxNTczODQxNzA2LCJleHAiOjE1NzQ0NDY1MDZ9.T-fOvOyHXjfJ3YdEqLMzxiibsNEGiL7qfkbdZEfq-5dhuJeJsSUyUwo9ufi7UzMs8dkAFJz89L8x9xou-HHQoZD_BQKkNwGJO9fZxwsxyZlXvV2dMvfSjUDXzdwsVbXSoV4EXsihyzSqbsCRAx6a_aGv49lxT1D5Rl6W3lxgR0uB12lZaP5Jv8ZPjnk7pOWv2oDJWdQ9yMeQ_JGAblVamn6eo1xktmfAjrJKnoMLZmmrTSAb6z0mGzKJ9OnckyfHl2psIrVNdlQrKvt-ITGk2Kyv_1TMYMHn14z1VxE9QZrFVOYRLqwpjCMVm7i0ac5ZQWUXbBn8YwY-UVFZ0wHBp7ox6kn0Gw6l7bVvKRsI62ip696aw8CtvwN-9pdE2JZVxmhUs3tua6FsoHYmdebkt4W-WsaNs3s5Eahqm4R_MLddhX74ZzKz2WHq7r1Ixd5P1_ArX4jSXvEwcJJVlE4PE1DMFvAP1QrgNCD-wPGm9OHnyQ0zXMGZ3boahklvVRvP_4qeP3xt1pgd6Bov8FxmmeT_EbTUc0GjetA9GOkmwRIB-Jrc80mf2OTrc8HA917ALllC9iprIFey6P2GaNCM7o46UEGsevd2Zku3ZMUVNCaz2T6TO4IcakvNDv-jG6qrZJurv20ARj_emJghX25nfxhFp70tO0yMlquxBh73XCo'}

# Parameter for the request reading
params = (
    ('devices', '109'), # The Sensor device value
    ('pageSize', '20'),
    ('pageIndex', '0'), # LEAVE AS IT IS
    ('readings', 'false'),
    ('context', 'true'),
    ('last', 'true'),
    ('grouped', 'false'),
    ('calculateAverage', 'true'),

)

# GET request
response = requests.get('https://api.nanovision.com/readings', headers=headers, params=params)

# Test: Print the response in a json format
print(json.dumps(response.json(), indent=5, sort_keys=True))

# Variables are defined to allow the eval() function to function
null = None
false = False
true = True
device_response=eval(response.text)

# Normalize the device response and assign them to a dataframe
response_table = (json_normalize(device_response['stats']))

# Rename rows
response_table.rename(index={
    0:'Temperature',
    1:'Humidity',
    2:'PM2.5',
    3: 'PM10.0',
    4: 'O3',
    5: 'CO2',
    6: 'Gas Resistance',
    7: 'Pressure',
    8: 'BME680_TEMP_C_DEC - Temperature_C',
    9: 'BME680_HUMIDITY_DEC - Relative_Humidity_%',
    10: 'AQI',
    11: 'Red Resistance Ratio',
    12: 'Ox Resistance Ratio',
    13: 'NH3 Resistance Ratio'
    },inplace=True)

# Format tables
response_table['average'] = response_table['average'].map('{:.2f}'.format)
response_table = response_table.drop(columns='lower_bound')
response_table = response_table.drop(columns='upper_bound')
response_table = response_table.rename(columns={'average':'value'})


# response_table = response_table.getfunction(line='PM2.5'.format)
# response_table = reponse_table.loadfunction(columns = 'average':'data_time')
# response_table = sort_keys_normalized(delta.time = '5')   in order to calcualte the simulation time.
# json.JSONDecodeError(msg, doc, pos,lineno. colno)


# Print table



