#########################################################
#           Large Data Request Script                   #
#########################################################
# Import Libraries
import requests
import jinja2
import ast
from datetime import datetime
from Tools.scripts.dutree import display
from pandas.io.json import json_normalize
import pandas as pd
import json
import os

# Set the table size for view
pd.set_option('display.width', 1000)
pd.set_option('display.max_row', 500)
pd.set_option('display.max_columns', 500)


#########################################################
# Dump method
def json_dump(page_index: int):
    # Header for the request
    headers = {
        'accept': 'application/json',
        # Authorization token
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJfaWQiOiI1NjUzODUyNjAyNzYxMjE2IiwiZmlyc3ROYW1lIjoiUENDSSIsImxhc3ROYW1lIjoiVGVzdCIsImVtYWlsIjoiZGV2ZWxvcGVyc19uYW5vQHBjY2lubm92YXRpb24ub3JnIiwiaWF0IjoxNTc1NDA1NTczLCJleHAiOjE1NzYwMTAzNzN9.VJsTS6lk4KypAV3DjH_6Ti6uF6JXMgNXixR7BpfMO4Lu_RExoA4Ona14jTnQG-n2wuGylWM-swkgj6WHyMtZUGIl5zjQ6uZ4Tlu1byrsDCXwtTM5SDN8oJ74xHxz3AzFlykSY65w7wWLXn9Eg89Akhgbje41C85YRxa_Wv0m5C3co0ZqaaQiYzKsK23eronjfpKuv7u9g4qDDP1gAaJwEl-yXi3Xy3B9-zmBTOn-iFKgkTIomKoCnG52tzFzjcp6EQMjdoIJxseDhsxbGv0IYqHbnnXC6I00swzYDg_Il5Df7dVZvBc5PNyNbTvX_5MYl6itFumYOLCjqxKCAv77CXVBrX8jCIHmW8uaI0jgpbx5TqzYrZX8MmSntt5uj_9mVctIVTibKg6wsQ7i8J3jRe83zZ8izIoKlpxH9CTi4nlJOZlbs72hi17loH5IqcOfbd6nsQeUMTMer0G7lCAMNWRSJSPZzFZwouVmHObWbUzv2hJ-xkgReyS1orJ-yX1F8EIvSQ_j_VOG17fBGeNk1qPBLy-6nKuBJytotn9AfvcRjRWwfFT4hA8p0OQAHw3aU-1mGkuPp7AfO36uQv_kTYU4peEaCsICTB7nhkWnYi88EZ5by0Xv8kDAEchoK-xjxMkd3TKaXLO7pb7_Nqhct-oO02cGKQdRFv7IVtl27fk'}
    # Parameter for the device request reading
    params = (
        ('devices', '109'),
        ('pageSize', '20'),
        ('pageIndex', str(page_index)),
        # Test date
        ('since', '09-23-2019-18:00:00-00:00'),
        ('until', '09-24-2019-19:10:00-00:00'),  # Use current time stamp for final
        ('granularity', 'RAW'),
        ('readings', 'true'),
        ('context', 'true'),
        ('last', 'false'),
        ('grouped', 'false'),
        ('calculateAverage', 'false'),
    )

    response = requests.get('https://api.nanovision.com/readings', headers=headers, params=params)

    # Return the response in a json format
    # End method
    return (response.json())


#########################################################

#########################################################
# Append batch date to json file method
def append_batch_date(json_file, date):
    for i in json_file['readings']:
        i['batch_date'] = str(date.isoformat())
    # Return file
    # End method
    return json_file


#########################################################

# Get Batch Date
batch_date = datetime.now()
# Date print
print(batch_date)
# Generate file name
file_name = datetime.today().strftime('%H_%M_%S')
folder_name = datetime.today().strftime('%y_%m_%d')
file_name = file_name + "_raw" + ".json"

# Make folder based on date in data
# Generate folder
try:
    os.mkdir("data/" + folder_name)
except OSError:
    print("Failed to create the directory at path, it could already exists?")
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
    #print(page_index)
    # Get response based on the page index value
    response_page = (json_dump(page_index))
    response_page = append_batch_date(response_page, batch_date)
    # Write formatted data to a json file
    file_handle.write('\n')
    # file_handle.write('[')
    file_handle.write('\n')
    file_handle.write(json.dumps(response_page, indent=5, sort_keys=True))
    file_handle.write('\n')
    # file_handle.write(']')
    file_handle.write('\n')
    # Check if there a next page
    if response_page['next'] == None:
        # Set Exit Coniditon and close file
        has_next = False
        file_handle.write(']')
        file_handle.close()
    else:
        file_handle.write(',')
#########################################################
# Get the current current date
# Generate a file and folder name based on the current time and date.
# iteratively submit a GET request using an incremental page number
# iteratively write each result to a JSON file
