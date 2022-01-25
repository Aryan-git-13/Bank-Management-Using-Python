import sqlite3
con = 0
#con = sqlite3.connect('Data.sqlite3')
while(con):
    print("Connection Established")
    break
else:
    print("not connected")
