import sqlite3

conn = sqlite3.connect('testing.db')
cur=conn.cursor()

#Checking that if the table exists earlier then do not create new table
list_of_table= cur.execute('''select tbl_name from sqlite_master
                                where type='table' and tbl_name= 'activity' ''').fetchall()

if list_of_table == []:
    #creating Table
    query_toCreateTable = '''
                        Create Table activity(
                            userId varchar(400),
                            activityStatus varchar(50),
                            captureTime varchar(50),
                            workBreakType varchar(50),
                            appName varchar(50),
                            webUrlTitle varchar(50),
                            webFullUrl varchar(50))
                            '''
    cur.execute(query_toCreateTable)
    
else:
    print("Table already exists")