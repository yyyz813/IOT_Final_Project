#########################################################
#           Synthetic data generation Script            #
#########################################################
import sys, os
import random
import json
import numpy as np
from datetime import timedelta, datetime as dt
from mimesis.schema import Field, Schema
import json
from datetime import datetime
_ = Field('en')
null = None

#########################################################
# Iteration value will determine the number of data sets that the synthetic data generation script will generate.
## Each set of data has 14 property id.
iterations_value = 1
#########################################################

# Device set up
# device_number will the hold the device id number
device_number = random.choice([108, 109])
# ts_value will hold the time stamp value which will be based on the time the synthetic data script is ran.
# ts_value represent the time the data were collected from by the device.
ts_value = (
    str(dt.now() - timedelta(_('numbers.integers', start=1, end=4, length=1)[0])).replace(' ', 'T')[:-6].replace('.',
                                                                                                                 'Z'))
# batch_value will hold the time stamp value which will be based on the time the synthetic data script is ran with 200 hour subracted from it.
# batch_value represent the time the data were collected from by the script.
batch_value = (
    str((dt.now() - timedelta(hours=200)) - timedelta(_('numbers.integers', start=1, end=4, length=1)[0])).replace(' ',
                                                                                                                   'T')[
    :-6].replace('.', 'Z'))
# The data format
description = (
    lambda: {

        "next": "devices=" + str(
            device_number) + "&pageSize=20&since=09-23-2019-18:00:00-00:00&until=09-24-2019-19:10:00-00:00&granularity=RAW&readings=true&context=true&last=false&grouped=false&calculateAverage=false&pageIndex=1",
        "previous": null,
        # Determine the status of the synthetic data
        # "synthetic" - Implies that the data in the json file are generated using a script
        # "corrupt" - Implies weather
        "synthetic_status": True,
        "corrupt_status": False,
        "readings": [

            {
                "batch_date": batch_value,

                "device_id": device_number,
                "property_id": json.dumps(_('numbers.integers', start=23, end=23, length=1)[0]),
                "sensor_id": json.dumps(_('numbers.integers', start=12, end=12, length=1)[0]),
                "ts": ts_value,
                "value": json.dumps(round(_('numbers.integers', start=20, end=50, length=1)[0] * .91, 2))
            }
            ,
            {
                "batch_date": batch_value,

                "device_id": device_number,
                "property_id": json.dumps(_('numbers.integers', start=24, end=24, length=1)[0]),
                "sensor_id": json.dumps(_('numbers.integers', start=12, end=12, length=1)[0]),
                "ts": ts_value,
                "value": json.dumps(round(_('numbers.integers', start=20, end=50, length=1)[0] * .91, 2))
            }
            ,
            {
                "batch_date": batch_value,

                "device_id": device_number,
                "property_id": json.dumps(_('numbers.integers', start=25, end=25, length=1)[0]),
                "sensor_id": json.dumps(_('numbers.integers', start=12, end=12, length=1)[0]),
                "ts": ts_value,
                "value": json.dumps(round(_('numbers.integers', start=10, end=90, length=1)[0] * .91, 2))
            }
            ,
            {
                "batch_date": batch_value,

                "device_id": device_number,
                "property_id": json.dumps(_('numbers.integers', start=26, end=26, length=1)[0]),
                "sensor_id": json.dumps(_('numbers.integers', start=12, end=12, length=1)[0]),
                "ts": ts_value,
                "value": json.dumps(round(_('numbers.integers', start=10, end=90, length=1)[0] * .91, 2))
            }
            ,
            {
                "batch_date": batch_value,

                "device_id": device_number,
                "property_id": json.dumps(_('numbers.integers', start=27, end=27, length=1)[0]),
                "sensor_id": json.dumps(_('numbers.integers', start=12, end=12, length=1)[0]),
                "ts": ts_value,
                "value": json.dumps(round(_('numbers.integers', start=100, end=200, length=1)[0] * .91, 2))
            }
            ,
            {
                "batch_date": batch_value,

                "device_id": device_number,
                "property_id": json.dumps(_('numbers.integers', start=28, end=28, length=1)[0]),
                "sensor_id": json.dumps(_('numbers.integers', start=12, end=12, length=1)[0]),
                "ts": ts_value,
                "value": json.dumps(round(_('numbers.integers', start=500, end=1000, length=1)[0] * .91, 2))
            }
            ,
            {
                "batch_date": batch_value,

                "device_id": device_number,
                "property_id": json.dumps(_('numbers.integers', start=29, end=29, length=1)[0]),
                "sensor_id": json.dumps(_('numbers.integers', start=12, end=12, length=1)[0]),
                "ts": ts_value,
                "value": json.dumps(round(_('numbers.integers', start=50, end=100000, length=1)[0] * .91, 2))
            }
            ,
            {
                "batch_date": batch_value,

                "device_id": device_number,
                "property_id": json.dumps(_('numbers.integers', start=30, end=30, length=1)[0]),
                "sensor_id": json.dumps(_('numbers.integers', start=12, end=12, length=1)[0]),
                "ts": ts_value,
                "value": json.dumps(round(_('numbers.integers', start=50000, end=100000, length=1)[0] * .91, 2))
            }
            ,
            {
                "batch_date": batch_value,

                "device_id": device_number,
                "property_id": json.dumps(_('numbers.integers', start=31, end=31, length=1)[0]),
                "sensor_id": json.dumps(_('numbers.integers', start=12, end=12, length=1)[0]),
                "ts": ts_value,
                "value": json.dumps(round(_('numbers.integers', start=20, end=60, length=1)[0] * .91, 2))
            }
            ,
            {
                "batch_date": batch_value,

                "device_id": device_number,
                "property_id": json.dumps(_('numbers.integers', start=32, end=32, length=1)[0]),
                "sensor_id": json.dumps(_('numbers.integers', start=12, end=12, length=1)[0]),
                "ts": ts_value,
                "value": json.dumps(round(_('numbers.integers', start=20, end=60, length=1)[0] * .91, 2))
            }
            ,
            {
                "batch_date": batch_value,

                "device_id": device_number,
                "property_id": json.dumps(_('numbers.integers', start=33, end=33, length=1)[0]),
                "sensor_id": json.dumps(_('numbers.integers', start=12, end=12, length=1)[0]),
                "ts": ts_value,
                "value": json.dumps(round(_('numbers.integers', start=10, end=100, length=1)[0] * .91, 2))
            }
            ,
            {
                "batch_date": batch_value,

                "device_id": device_number,
                "property_id": json.dumps(_('numbers.integers', start=34, end=34, length=1)[0]),
                "sensor_id": json.dumps(_('numbers.integers', start=12, end=12, length=1)[0]),
                "ts": ts_value,
                "value": json.dumps(round(_('numbers.integers', start=500000, end=1500000, length=1)[0] * .91, 2))
            }
            ,
            {
                "batch_date": batch_value,

                "device_id": device_number,
                "property_id": json.dumps(_('numbers.integers', start=35, end=35, length=1)[0]),
                "sensor_id": json.dumps(_('numbers.integers', start=12, end=12, length=1)[0]),
                "ts": ts_value,
                "value": json.dumps(round(_('numbers.integers', start=20000, end=75000, length=1)[0] * .91, 2))
            }
            ,
            {
                "batch_date": batch_value,

                "device_id": device_number,
                "property_id": json.dumps(_('numbers.integers', start=36, end=36, length=1)[0]),
                "sensor_id": json.dumps(_('numbers.integers', start=12, end=12, length=1)[0]),
                "ts": ts_value,
                "value": json.dumps(round(_('numbers.integers', start=650000, end=1350000, length=1)[0] * .91, 2))
            }

        ],

        # To get accurate number of total reading the iterations_value is multiplied by 14 ( The number of property ids )
        "total_readings": (14 * iterations_value)

    }
)

#########################################################
schema = Schema(schema=description)
for i in range(5):
    # Create a set of data based on the iterations_value
    schema_output = schema.create(iterations=iterations_value)
# Print the formated json output
#print(json.dumps(schema_output, sort_keys=True, indent=4))

#########################################################
# Write to file
# Generate Name
date = datetime.now()
print(date)
folder_name = date.today().strftime('%y_%m_%d') # # folder name that contain the file to be parsed
file_name = date.today().strftime('%H_%M_%S') + '_raw_synthetic.json' # file name to be parsed
folder_path = 'synthetic/' + folder_name
file_path = folder_path + '/' + file_name
# Check if the data folder exists
if not os.path.exists("synthetic"):
    # Make folder based on date in data
    # Generate folder
    try:
        os.mkdir("synthetic")
    except OSError:
        print("Failed to create the \"synthetic\" directory at path")
if not os.path.exists("synthetic/" + folder_name):
    try:
        os.mkdir("synthetic/" + folder_name)
    except OSError:
        print("Failed to create the \"" + folder_name + "\" directory at path")

 # Test: Print file name and path folder

file_handler = open(file_path, 'w+')
file_handler.write(json.dumps(schema_output, sort_keys=True, indent=4))
file_handler.close()
#########################################################

batch.time = os.mkdir("Fail to create the data enviornment")