#2.
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Sukanya@2003',database='Inventory_Management')
print(mydb.connection_id)
cur=mydb.cursor()

# creating the manufacture table
cur.execute('create table manufacture(manufacture_id INTEGER PRIMARY KEY,defective_items INTEGER(5),item_name VARCHAR(20),company VARCHAR(20),item_color VARCHAR(30),quantity INTEGER(5)')


# creating the goods table
cur.execute('create table goods(goods_id INTEGER(5)PRIMARY KEY,manufactured_date DATE,manufacture_id INTEGER,FOREIGN KEY(manufacture_id) REFERENCES manufacture(manufacture_id)')

# creating purchase table
cur.execute('create table purchase(purchase_id INTEGER(5) PRIMARY KEY,purchase_amt INTEGER,store_name VARCHAR(30),purchase_date DATE)')

# creating sale table
cur.execute('create table sale(sale_id INTEGER(5) PRIMARY KEY,sale_date DATE,profit_margin FLOAT,store_name VARCHAR(30),goods_id INTEGER(5),FOREIGN KEY(goods_id) REFERENCES goods(goods_id))')
