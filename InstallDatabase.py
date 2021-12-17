#########################################################
#     Database connection  and insert operation         #
#########################################################
# Import Libraries
import psycopg2

#########################################################
# url set up
try:
    conn = psycopg2.connect("dbname='nano' user='postgres' host='localhost' password='4257799'")
except ConnectionError:
    print("I am unable to connect to the database")
    exit(-1)

cur = conn.cursor()


#########################################################
# Run SQL Script method
def execute_sql(script_path):
    print("Executing " + script_path)

    # Do we need error checking with try/except?
    cur.execute(open(script_path, "r").read())


#########################################################

#####################################################################
# url format                                                        #
# postgresql://name:password@localhost:5432/nano                    #
# Change name and password to match the localhost / host set up     #
# change localhost to match the database in use                     #
#####################################################################
database_name = ["Nano_DEV",
                 "Nano_TEST",
                 "Nano_QA",
                 "Nano_PROD"]

create_sequence = ["Create/CREATE.AUDIT.LOGGED_ACTIONS.sql",
                   "Create/CREATE.LKP.DEVICE.sql",
                   "Create/CREATE.LKP.SENSOR.sql",
                   "Create/CREATE.LKP.PROPERTY.sql",
                   "Create/CREATE.FCT.RECORDS.sql",
                   "Create/CREATE.RAW.NANO.sql",
                   "Create/CREATE.RAW.SYNTHETIC.sql"]

load_sequence = ["Load/LOAD.LKP.DEVICE.sql",
                 "Load/LOAD.LKP.SENSOR.sql",
                 "Load/LOAD.LKP.PROPERTY.sql",
                 "Load/LOAD.FCT.RECORDS.sql"]

# Execute query method
for file in create_sequence:
    execute_sql(file)

for file in load_sequence:
    execute_sql(file)

conn.commit()