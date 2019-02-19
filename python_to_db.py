import MySQLdb

""" setting MySQL """
db = MySQLdb.connect(host="localhost", user="OWNER", passwd="12345", db="prototype_lab")
#create a cursor for the select
cur = db.cursor()
sql = 'show tables'
cur.execute(sql)
print(cur.fetchall())

command=raw_input("enter command 1: insert data 2:get data\n")
#print(command+command)
if command=="1":
    #data_to_local_db_TAPLE = ("A,A,A")
    print(1)
    table_name=raw_input("enter table name\n")
    print(1)
    if table_name=='Employee':
        data_list=raw_input("enter 'EmployeeId','Name','EmployeeDept',iBeaconID\n")
        #print("""INSERT INTO Employee (EmployeeId, Name, EmployeeDept, iBeaconID) VALUES("""+data_list+""")""")
        cur.execute("""INSERT INTO Employee (EmployeeId, Name, EmployeeDept, iBeaconID) VALUES("""+data_list+""")""")


    if table_name=='MeetingRoom':
        data_list=raw_input("enter RoomNo,Capacity,Floor")
        cur.execute("""INSERT INTO MeetingRoom (RoomNo, Capacity, Floor) VALUES("""+data_list+""")""")


    if table_name=='Book':
        data_list=raw_input("enter BookNo,Name,TagId")
        cur.execute("""INSERT INTO MeetingRoom (BookNo,Name,TagId) VALUES("""+data_list+""")""")


    if table_name=='BookMonitoringSystem':
        data_list=raw_input("enter date,Bookno,EmployeeId,statement")
        cur.execute("""INSERT INTO BookMonitoringSystem(monitoring date, BookNo, EmployeeId, statement) VALUES("""+data_list+""")""")


    if table_name=='MovementMonitoringSystem':
        data_list=raw_input("enter date,Room,EmployeeId,statement")
        cur.execute("""INSERT INTO BookMonitoringSystem(date,Room,BookNo, EmployeeId, statement) VALUES("""+data_list+""")""")

    db.commit()

    # close the cursor
    cur.close()

    # close the DB connection
    db.close ()
num_count=0
if command == "2":
    #print(2)
    command_2=raw_input("1:check number of people\n")
    #print(3)
    if command_2=="1":
        cur.execute("SELECT * FROM MovementMonitoringSystem AS m WHERE date = ( SELECT MAX(date) FROM MovementMonitoringSystem AS s WHERE m.Room = s.Room);")
        rows = cur.fetchall()
        for row in rows:
            print(row)
            if row[3]=="exist":
                print(row[3])
                num_count = num_count+1
        print(num_count)
            
        cur.close()
        db.close()
