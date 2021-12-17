#########################################################
#           Large Data Request Script                   #
#########################################################
# Import Libraries
import requests
import jinja2
import ast
from datetime import datetime
from datetime import timedelta
from Tools.scripts.dutree import display
from pandas.io.json import json_normalize
import pandas as pd
import json
import os
import os.path
import dateutil
#########################################################
#     Database connection  and insert operation         #
#########################################################
# Import Libraries
import ijson
import sqlalchemy
from sqlalchemy_utils import database_exists
from sqlalchemy import create_engine
from sqlalchemy import func
import psycopg2
from psycopg2 import connect
from psycopg2 import _psycopg

#########################################################


#########################################################
# Get Batch Date
batch_date = datetime.now()
#########################################################
# Set the parameter dates value
# Current time
until_date = (batch_date + timedelta(
    hours=6)).strftime('%m-%d-%y-%H:%M:%S') + '-00:00'
# Current time minus one hour
batch_date_past_since = (batch_date + timedelta(
    hours=6)) - timedelta(
    minutes=5)  # For testing purposes subtract an 2 minuts  ( Final could be an hour or 30 Minutes ) # Cant be the same time
since_date = batch_date_past_since.strftime('%m-%d-%y-%H:%M:%S') + '-00:00'
# Set the table size for view
pd.set_option('display.width', 1000)
pd.set_option('display.max_row', 500)
pd.set_option('display.max_columns', 500)

print('until_date ' + until_date)
print('since_date ' + since_date)



#########################################################
# A method to refersh the nano dashboard token
def refresh_token(old_token: str) -> str:
    # Header for the request
    headers = {
        'accept': 'application/json',
        # Authorization token

    }

    params = {
        'email': 'developers_nano@pccinnovation.org',
        'password': 'NanoDeviceSetup2019'
    }
    print(params)
    response = requests.post('https://fumus-auth-dot-cloud-prd.appspot.com/api/auth/login', headers=headers,
                             params=params)
    print(response.json()['token'])
    token = response.json()['token']
    return token


#########################################################
# Dump method
def json_dump(page_index: int):
    # Header for the request
    headers = {
        'accept': 'application/json',
        # Authorization token e is x x is e
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJfaWQiOiI1NjUzODUyNjAyNzYxMjE2IiwiZmlyc3ROYW1lIjoiUENDSSIsImxhc3ROYW1lIjoiVGVzdCIsImVtYWlsIjoiZGV2ZWxvcGVyc19uYW5vQHBjY2lubm92YXRpb24ub3JnIiwiaWF0IjoxNTc1NDA1NTczLCJleHAiOjE1NzYwMTAzNzN9.VJsTS6lk4KypAV3DjH_6Ti6uF6JXMgNXixR7BpfMO4Lu_RExoA4Ona14jTnQG-n2wuGylWM-swkgj6WHyMtZUGIl5zjQ6uZ4Tlu1byrsDCXwtTM5SDN8oJ74xHxz3AzFlykSY65w7wWLXn9Eg89Akhgbje41C85YRxa_Wv0m5C3co0ZqaaQiYzKsK23eronjfpKuv7u9g4qDDP1gAaJwEl-yXi3Xy3B9-zmBTOn-iFKgkTIomKoCnG52tzFzjcp6EQMjdoIJxseDhsxbGv0IYqHbnnXC6I00swzYDg_Il5Df7dVZvBc5PNyNbTvX_5MYl6itFumYOLCjqxKCAv77CXVBrX8jCIHmW8uaI0jgpbx5TqzYrZX8MmSntt5uj_9mVctIVTibKg6wsQ7i8J3jRe83zZ8izIoKlpxH9CTi4nlJOZlbs72hi17loH5IqcOfbd6nsQeUMTMer0G7lCAMNWRSJSPZzFZwouVmHObWbUzv2hJ-xkgReyS1orJ-yX1F8EIvSQ_j_VOG17fBGeNk1qPBLy-6nKuBJytotn9AfvcRjRWwfFT4hA8p0OQAHw3aU-1mGkuPp7AfO36uQv_kTYU4peEaCsICTB7nhkWnYi88EZ5by0Xv8kDAEchoK-xjxMkd3TKaXLO7pb7_Nqhct-oO02cGKQdRFv7IVtl27fk'}

    # Parameter for the device request reading
    params = (
        ('devices', '109'),  # device number
        ('pageSize', '20'),
        ('pageIndex', str(page_index)),
        # Test date
        ('since', since_date),
        ('until', until_date),  # Use current time stamp for final batch_date

        ('granularity', 'MINUTE'),
        ('readings', 'true'),
        ('context', 'true'),
        ('last', 'false'),
        ('grouped', 'true'),  # was false
        ('calculateAverage', 'false'),
    )

    response = requests.get('https://api.nanovision.com/readings', headers=headers, params=params)

    # Refresh the token
    # if the Unauthorized access message is return in the response
    # Attempt to update the token and generate  new response
    if 'error' in response.json():  # if (True): use to test
        if (response.json()['error']['message'] == 'Unauthorized'):  # if (True): use to test
            print("Unauthorized Response Message - Token might be expired")
            # Refresh token with refresh   method
            print("Old header " + headers['Authorization'])
            new_header: str = refresh_token(headers['Authorization'])
            print(" New header " + new_header)
            headers['Authorization'] = new_header
            response = requests.get('https://api.nanovision.com/readings', headers=headers, params=params)

    # Return the response in a json format
    # End method
    return (response.json())


#########################################################

#########################################################
# Append batch date to json file method
def append_batch_date(json_file, date):
    if 'readings' in json_file:
        for i in json_file['readings']:
            i['batch_date'] = str(date.isoformat())
            #############
            # print('---')
            # print(i['ts'])
            date_changer = dateutil.parser.parse(i['ts'])
            #  print(  date_changer)
            new_ts = str((date_changer - timedelta(hours=6)).isoformat())
            # print(new_ts)
            i['ts'] = new_ts
            #############
    # Return file
    # End method
    return json_file


#########################################################

#########################################################
# Parse and insert method
def parse_file(path_name):
    # Counter
    i = 0
    # Parse file iteratively
    file_handler = open(path_name, 'rb')
    # readings = ijson.items(file_handler, 'readings.item')
    # Expected variable from file
    # "batch_date": " ",
    # "device_id":  ,
    # "property_id":  ,
    # "sensor_id":  ,
    # "ts": " ",
    # "value":
    for id in ijson.items(file_handler, 'item.readings.item'):  # item -> idicate a list
        var_batch_date = str(id['batch_date'])
        var_device_id = str(id['device_id'])
        var_property_id = str(id['property_id'])
        var_sensor_id = str(id['sensor_id'])
        var_ts = str(id['ts'])
        var_value = str(id['value'])
        # assign each property to variable
        # execute statment
        i = i + 1
        # Prepared statement
        str_insert = db_connection.execute('''INSERT INTO raw.nano (device_id,sensor_id,property_id,value,time_stamp,batch_date) 
            VALUES (%s,%s,%s,%s,%s,%s)''', var_device_id, var_sensor_id, var_property_id, var_value, var_ts,
                                           var_batch_date)

    # Print the number of inserts
    print(i)
    # Close file
    file_handler.close()
    # End method


#########################################################


# Date print
print(batch_date)
# Generate file name
file_name = datetime.today().strftime('%H_%M_%S')
folder_name = datetime.today().strftime('%y_%m_%d')
file_name = file_name + "_raw" + ".json"

# Check if the data folder exists
if not os.path.exists("data"):
    # Make folder based on date in data
    # Generate folder
    try:
        os.mkdir("data")
    except OSError:
        print("Failed to create the \"data\" directory at path")
if not os.path.exists("data/" + folder_name):
    try:
        os.mkdir("data/" + folder_name)
    except OSError:
        print("Failed to create the \"" + folder_name + "\" directory at path")

path = "data/" + folder_name + "/" + file_name
# Test: Print file name and path folder
print(file_name)
print(path)

# Set json file index
page_index = -1
# open json file to write to
file_handle = open(path, "w+")
# set the start of the json file
file_handle.write('[')
file_handle.write('\n')
# Loop condition
has_next = True
while has_next:
    # Page index
    page_index = page_index + 1
    # print(page_index)
    # Get response based on the page index value
    response_page = (json_dump(page_index))
    # print(page_index)# test var
    response_page = append_batch_date(response_page, batch_date)
    # Write formatted data to a json file
    file_handle.write('\n')
    # file_handle.write('[')
    file_handle.write('\n')
    file_handle.write(json.dumps(response_page, indent=5, sort_keys=True))
    #############

    #############
    file_handle.write('\n')
    # file_handle.write(']')
    file_handle.write('\n')

    # Check if there a next page
    if 'next' in response_page:
        if response_page['next'] == None:
            # Set Exit Coniditon and close file
            has_next = False
            file_handle.write(']')
            file_handle.close()
        else:
            file_handle.write(',')
    else:
        break
#########################################################
# Get the current current date
# Generate a file and folder name based on the current time and date.
# iteratively submit a GET request using an incremental page number
# iteratively write each result to a JSON file
#########################################################
# url set up
url = 'postgresql://postgres:4257799@localhost:5432/nano'  # N do database name and password to inputed variable
# create engine
db_connection = create_engine(url)
# if nano database does not exists then exit
if not database_exists(url):
    print("Error: Database dose not exists")
    exit(-1)
# if the table  does not exists
if not db_connection.dialect.has_table(db_connection, 'nano', 'raw'):  # modifiy name
    print("Error: Database table raw.nano dose not exists")
    exit(-1)

#####################################################################
# url format                                                        #
# postgresql://name:password@localhost:5432/nano                    #
# Change name and password to match the localhost / host set up     #
# change localhost to match the database in use                     #
#####################################################################
print(db_connection)
print(batch_date.strftime('%m_%d_%y_%H_%M_%S'))
date_folder = batch_date.strftime('%y_%m_%d')  # # folder name that contain the file to be parsed
date_file = batch_date.strftime('%H_%M_%S') + '_raw.json'  # file name to be parsed
path = 'data/' + date_folder
path_name = path + '/' + date_file
# Execute query method
parse_file(path_name)
######################################################
# Load the data from raw table into the records table to be used by POWER BI
######################################################
con = psycopg2.connect(url)
print(con)
cur = con.cursor()
print(cur)
cur.execute('CALL admin.load_fct_records()')
cur.close()
con.commit()
con.close()
######################################################
# Testing refersh
print(refresh_token(
    'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJfaWQiOiI1NjUzODUyNjAyNzYxMjE2IiwiZmlyc3ROYW1lIjoiUENDSSIsImxhc3ROYW1lIjoiVGVzdCIsImVtYWlsIjoiZGV2ZWxvcGVyc19uYW5vQHBjY2lubm92YXRpb24ub3JnIiwiaWF0IjoxNTc1NDA1NTczLCJleHAiOjE1NzYwMTAzNzN9.VJsTS6lk4KypAV3DjH_6Ti6uF6JXMgNXixR7BpfMO4Lu_RExoA4Ona14jTnQG-n2wuGylWM-swkgj6WHyMtZUGIl5zjQ6uZ4Tlu1byrsDCXwtTM5SDN8oJ74xHxz3AzFlykSY65w7wWLXn9Eg89Akhgbje41C85YRxa_Wv0m5C3co0ZqaaQiYzKsK23eronjfpKuv7u9g4qDDP1gAaJwEl-yXi3Xy3B9-zmBTOn-iFKgkTIomKoCnG52tzFzjcp6EQMjdoIJxseDhsxbGv0IYqHbnnXC6I00swzYDg_Il5Df7dVZvBc5PNyNbTvX_5MYl6itFumYOLCjqxKCAv77CXVBrX8jCIHmW8uaI0jgpbx5TqzYrZX8MmSntt5uj_9mVctIVTibKg6wsQ7i8J3jRe83zZ8izIoKlpxH9CTi4nlJOZlbs72hi17loH5IqcOfbd6nsQeUMTMer0G7lCAMNWRSJSPZzFZwouVmHObWbUzv2hJ-xkgReyS1orJ-yX1F8EIvSQ_j_VOG17fBGeNk1qPBLy-6nKuBJytotn9AfvcRjRWwfFT4hA8p0OQAHw3aU-1mGkuPp7AfO36uQv_kTYU4peEaCsICTB7nhkWnYi88EZ5by0Xv8kDAEchoK-xjxMkd3TKaXLO7pb7_Nqhct-oO02cGKQdRFv7IVtl27fk'))

json_dump(page)