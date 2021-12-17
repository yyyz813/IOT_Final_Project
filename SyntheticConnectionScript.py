###########################################################################
#     Database connection  and insert operation for Synthetic data        #
###########################################################################
# Import Libraries
import ijson
import sqlalchemy
from sqlalchemy_utils import database_exists
from sqlalchemy import create_engine

#########################################################
# url set up
url = 'postgresql://postgres:4257799@localhost:5432/nano'#N do database name and password to inputed variable
# create engine
db_connection = create_engine(url)
# if nano database does not exists then exit
if not database_exists(url):
    print("Error: Database dose not exists")
    exit(-1)
# if raw.nano table  does not exists
if not  db_connection.dialect.has_table(db_connection,'synthetic','raw'):
    print("Error: Database table raw.synthetic dose not exists")
    exit(-1)

#########################################################
# Parse and insert method
def parse_file(path_name):
    # Counter
    i = 0
    # Parse file iteratively
    file_handler = open(path_name, 'rb')
     # Expected variable from file
    # "batch_date": " ",
    # "device_id":  ,
    # "property_id":  ,
    # "sensor_id":  ,
    # "ts": " ",
    # "value":
    # --------
    # "synthetic":
    # "corrupt":

    var_synthetic =   ijson.items(file_handler, 'item.synthetic_status')
    for obj_synthetic in var_synthetic:
        print(str(obj_synthetic))
        var_synthetic = str(obj_synthetic)
    # Need to reset the file handler to 0 else the file will be read incorrectly due to incorrectly position iterator
    file_handler.seek(0)
    var_corrupt =  ijson.items(file_handler, 'item.corrupt_status')
    for obj_corrupt in var_corrupt:
        print(str(obj_corrupt))
        var_corrupt = str(obj_corrupt)
    # Need to reset the file handler to 0 else the file will be read incorrectly due to incorrectly position iterator
    file_handler.seek(0)
    for id in ijson.items(file_handler, 'item.readings.item'):  # item -> idicate a list
        var_batch_date = str(id['batch_date'])
        var_device_id = str(id['device_id'])
        var_property_id = str(id['property_id'])
        var_sensor_id = str(id['sensor_id'])
        var_ts = str(id['ts'])
        var_value = str(id['value'])
        # list - > object -> list ->object -> readings
        # assign each property to variable
        # execute statment
        i = i + 1
        # Prepared statement
        str_insert = db_connection.execute('''INSERT INTO raw.synthetic (device_id,sensor_id,property_id,value,time_stamp,batch_date,synthetic_data,corrupt_data) 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)''', var_device_id, var_sensor_id, var_property_id, var_value,var_ts, var_batch_date,var_synthetic,var_corrupt)

    # Print the number of inserts
    print("The Number of inserts: " + str(i))
    # Close file
    file_handler.close()
    # End method


#########################################################

#####################################################################
# url format                                                        #
# postgresql://name:password@localhost:5432/database_name           #
# Change name and password to match the localhost / host set up     #
# change localhost to match the database in use                     #
#####################################################################
print(db_connection)
# place holder
date_folder = '19_11_16' # # folder name that contain the file to be parsed
date_file = '20_04_00_raw_synthetic.json' # file name to be parsed
path = 'synthetic/' + date_folder
path_name = path + '/' + date_file
# Execute query method
parse_file(path_name)

