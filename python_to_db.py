import MySQLdb


""" setting MySQL """
db = MySQLdb.connect(host="localhost", user="OWNER", passwd="12345", db="prototype_lab")
#create a cursor for the select
cur = db.cursor()


cur.execute("""INSERT INTO Employee parameters (EmployeeId, Name, EmployeeDept, iBeaconID) VALUES(%s,%s,%s,%s)""", data_to_local_db_TAPLE)

cur.execute("""INSERT INTO MeetingRoom parameters (RoomNo, Capacity, Floor) VALUES(%s,%d,%d)""", data_to_local_db_TAPLE)
cur.execute("""INSERT INTO Book parameters (BookNo, Name, TagId) VALUES(%d,%s,%s)""", data_to_local_db_TAPLE)
cur.execute("""INSERT INTO Movement Monitoring System parameters (monitoring date, Place, EmployeeId, statement) VALUES(%s,%d,%s,%s)""", data_to_local_db_TAPLE)

cur.execute("""INSERT INTO Book Monitoring System parameters (monitoring date, BookNo, EmployeeId, statement) VALUES(%s,%d,%s,%s)""", data_to_local_db_TAPLE)

db.commit()

# close the cursor
cur.close()

# close the DB connection
db.close ()

