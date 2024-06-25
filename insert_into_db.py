def insertIntoDb(time_today, max_temp, min_temp, humidity): 
    import snowflake.connector
    import os 
    from dotenv import load_dotenv, dotenv_values 
    from datetime import datetime
    load_dotenv()
    # Gets the version
    snowflake.connector.paramstyle='qmark'

    print(time_today, max_temp, min_temp, humidity)
    conn = snowflake.connector.connect(
        user='SAMMMOW',
        password=os.getenv("snowflake_pw"),
        account='QRCZTZF-OY82487'
        )
    
    conn.cursor().execute("USE DATABASE testdb")

    conn.cursor().execute(
        "INSERT INTO test_table VALUES (?,?,?,?)",(("TIMESTAMP_NTZ",time_today), max_temp, min_temp, humidity)
    )

    conn.close()    
