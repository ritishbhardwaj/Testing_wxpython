import sqlite3

conn = sqlite3.connect('testing.db')
cur=conn.cursor()

#Checking that if the table exists earlier then do not create new table
list_of_table= cur.execute('''select tbl_name from sqlite_master
                                where type='table' and tbl_name= 'webcam' ''').fetchall()

if list_of_table == []:
    #creating Table
    query_toCreateTable = '''
                        Create Table webcam(
                            userId varchar(400),
                            captureTime varchar(50),
                            fileType varchar(50),
                            fileName varchar(50),
                            camerapic Blob)
                            '''
    cur.execute(query_toCreateTable)
    
else:
    print("Table already exists")

