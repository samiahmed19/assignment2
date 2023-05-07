#8.Update the manufacture details of all the red-colored toys which are purchased by the “MyKids” store.
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='samiA12,',database='Inventory_management')
cur=mydb.cursor()
t=" upadte manufacture color='red' where store='mykidstore'  "
cur.execute(t)
display=cur.fetchall()
for x in display:
    print(x)