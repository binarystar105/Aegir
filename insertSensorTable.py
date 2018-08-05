
import sqlite3
import sys
conn=sqlite3.connect('sensorsData.db')
curs=conn.cursor()


# function to insert data on a table
def add_data (PH, DOx, TMP):
    curs.execute("INSERT INTO Sensor_data values(datetime('now'), (?), (?), (?))", (PH, DOx, TMP))
    conn.commit()

# call the function to insert data
# curs.execute("DROP TABLE IF EXISTS Sensor_data")

add_data (9.1, 20.5, 36.1)
add_data (9.2, 25.8, 36.2)
add_data (9.4, 30.3, 36.8)

# print database content
print ("\nEntire database contents:\n")
for row in curs.execute("SELECT * FROM Sensor_data"):
    print (row)
# close the database after use
conn.close()