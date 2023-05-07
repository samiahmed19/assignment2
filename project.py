#1.Create a database called “Inventory_Management” with different tables like “manufacture”, “goods”, “purchase”, “sale” etc.
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='samiA12,'
)
print(mydb.connection_id)
mycrscr = mydb.cursor()
mycrscr.execute('CREATE DATABASE INVENTORY_MANAGEMENT')
#create table Inventory_Management;


#3.In the “manufacture” table, one should be able to see all the products that need to be manufactured, and defective items during the manufacture with different entries like manufacture id, number of items required, etc. 
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='samiA12,',
    database = 'INVENTORY_MANAGEMENT'
)
cur=mydb.cursor()
t = 'create table MANUFACTURE(id INTEGER(10) PRIMARY KEY,product_name VARCHAR(20),color VARCHAR(10),quantity INTEGER(10),manufacturing_date DATE,defective_ITEM VARCHAR(10),company_name varchar(20))'
cur.execute(t)
print("Table created succesfully")


#4.In the “goods” table, it should include different items that are manufactured by the company along with the goods id, manufactured date, etc.
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='samiA12,',
    database = 'INVENTORY_MANAGEMENT'
)
cur=mydb.cursor()
t = 'create table GOODS(g_id INTEGER(10),p_name varchar(10),color varchar(10),quantity integer(10),manufacturing_date date)'
cur.execute(t)
print("Table created succesfully")


#5.In the “purchase” table, it should include all the purchase details that are purchased in different online and offline stores, along with the purchase id, purchase amount, etc.
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='samiA12,',
    database = 'INVENTORY_MANAGEMENT'
)
cur=mydb.cursor()
t = 'create table PURCHASE(p_id INTEGER(10),store_name string,product_name varchar(10),color VARCHAR(10),qty INTEGER(10),p_amount INTEGER(20),p_date DATE)'
cur.execute(t)
print("Table created succesfully")


#6.In the “sale” table, it should include all the items got sold in different stores with the sale date, profit margin, etc
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='samiA12,',
    database = 'INVENTORY_MANAGEMENT'
)
cur=mydb.cursor()
t = 'create table SALE(s_id INTEGER(10),store_name VARCHAR(10),p_name VARCHAR(20),color VARCHAR(10),no_of_items INTEGER(10),sale_amount REAL,sale_date DATE,profit_margin real)'
cur.execute(t)
print("Table created succesfully")


#insertion values into tables 
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='samiA12,',
    database = 'INVENTORY_MANAGEMENT'
)
cur=mydb.cursor()
z = 'insert into MANUFACTURE(id,product_name,color,quantity,manufacturing_date,defective_ITEM,company_name) values(%s,%s,%s,%s,%s,%s,%s)'
a = [(1, 'Car', 'Red', 100, '01-04-23', 0,'RR export'),(2, 'Train', 'Green', 50, '01-04-23', 0,'SS Export'),(3, 'Wooden Chair', 'Brown', 200, '01-04-23', 0,'SS Export'),(4, 'Wooden Table', 'Brown', 100, '01-04-23', 0,'RR Export')]
cur.executemany(z,a)
mydb.commit()
print("Data inserted succesfully")


import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='samiA12,',
    database = 'INVENTORY_MANAGEMENT'
)
cur=mydb.cursor()
z = 'insert into GOODS(id,product_name,color,quantity,manufacturing_date) values(%s,%s,%s,%s,%s)'
a = [(1, 'Car', 'Red', 100, '01-04-23'),(2, 'Train', 'Green', 50, '01-04-23'),(3, 'Wood Chair', 'Brown', 200, '01-04-23'),(4, 'Wood Table', 'Brown', 100, '01-04-23')]
cur.executemany(z,a)
mydb.commit()
print("Data inserted succesfully")



import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='samiA12,',
    database = 'INVENTORY_MANAGEMENT'
)
cur=mydb.cursor()
z = 'insert into PURCHASE(id,store_name,product_name,color,quantity,purchase_amount,purchase_date) values(%s,%s,%s,%s,%s,%s,%s)'
a = [(1, 'MyKids', 'Car', 'Red', 50, 500, '01-05-23'),(2, 'MyKids', 'Train', 'Green', 25, 250, '01-05-23'),(3, 'ORay', 'Shirt', 'Blue',10,200,'01-05-23')]
cur.executemany(z,a)
mydb.commit()
print("Data inserted succesfully")



import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='samiA12,',
    database = 'INVENTORY_MANAGEMENT'
)
cur=mydb.cursor()
z = 'insert into SALE(id,store_name,product_name,color,no_of_items,sale_amount,sale_date,profit_margin) values(%s,%s,%s,%s,%s,%s,%s,%s)'
a = [(1, 'Offline', 'Car', 'Green', 100, 800, '2023-04-01',10),
(2, 'Online', 'Train', 'Green', 100, 800, '2023-01-05',12.2),
(3, 'Offlin', 'Wooden Chair', 'Green', 100, 800, '2023-04-10',15.6),
(4, 'Online', 'Wooden Table', 'Green', 100, 800, '2023-04-15',13.65),
(5, 'Offline', 'Train', 'Green', 100, 800, '2023-10-25',18.65)]
cur.executemany(z,a)
mydb.commit()
print("Data inserted succesfully")



#7.Delete the defective item, e.g., the shirt which was accidentally purchased by the “ORay” store, manufactured on the date ‘01-04-23’.
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='samiA12,',
    database = 'INVENTORY_MANAGEMENT'
)
cur=mydb.cursor()
t ="DELETE FROM purchase WHERE product_name = 'shirt' AND store_name = 'ORay' AND purchase_date = '2001-05-23'"
cur.execute(t)  
e = "select * from purchase"
cur.execute(e)  
print("Success")



#8.Update the manufacture details of all the red-colored toys which are purchased by the “MyKids” store.
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='samiA12,',
    database = 'INVENTORY_MANAGEMENT'
)
cur=mydb.cursor()
t ="UPDATE manufacture SET quantity = '50' WHERE color = 'Red'"
cur.execute(t)  
f= "select * from manufacture"
cur.execute(f)  
print("Success")



#9.Display all the “wooden chair” items that were manufactured before the 1st May 2023.
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='samiA12,',
    database = 'INVENTORY_MANAGEMENT'
)
cur=mydb.cursor()
t ="SELECT *FROM goods WHERE product_name = 'wood chair' AND manufacturing_date < '2001-05-23'"
cur.execute(t)  
print("Success")



#10.Display the profit margin amount of the “wooden table” that was sold by the “MyCare” store, manufactured by the “SS Export” company.
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password='samiA12,',
    database = 'INVENTORY_MANAGEMENT'
)
cur=mydb.cursor()
t ="SELECT profit_margin FROM sale WHERE product_name = 'wood table' AND store_name = 'Mykids' AND id IN (  SELECT id  FROM manufacture  WHERE company_name = 'SS Export')"
cur.execute(f)
print("Success")
