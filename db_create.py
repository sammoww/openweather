import snowflake.connector
import os 
from dotenv import load_dotenv, dotenv_values 

load_dotenv()
# Gets the version

conn = snowflake.connector.connect(
    user='SAMMMOW',
    password=os.getenv("snowflake_pw"),
    account='QRCZTZF-OY82487'
    )

conn.cursor().execute("USE DATABASE testdb")

conn.cursor().execute("CREATE SCHEMA IF NOT EXISTS testschema")


conn.cursor().execute(
    "CREATE OR REPLACE TABLE test_table(\
    timestamp timestamp_ltz,\
    max_temp float,\
    min_temp float,\
    humidity int)" #TIMESTAMP is for 1970 to 2038-01-19. DATETIME IS FOR TILL YEAR 9999. In this case, timestamp is efficient
)
