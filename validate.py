#!/usr/bin/env python
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
cs = conn.cursor()  

#initializing database and schema
#conn.cursor().execute("CREATE WAREHOUSE IF NOT EXISTS test_warehouse")
#conn.cursor().execute("CREATE DATABASE IF NOT EXISTS testdb")

conn.cursor().execute("USE DATABASE testdb")
conn.cursor().execute("SHOW SCHEMA")
try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
conn.close()