import sqlite3 as lite
import sys
con = lite.connect('sensorsData.db')
with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS Sensor_data")
    cur.execute("CREATE TABLE Sensor_data(timestamp DATETIME, PH NUMERIC, DOx NUMERIC,  TMP NUMERIC)")