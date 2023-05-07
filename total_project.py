#1.
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Sukanya@2003')
print(mydb.connection_id)
cur=mydb.cursor()
cur.execute("create database Inventory_Management")
cur.execute('use Inventory_Management')

#2.creating the manufacture table
cur.execute('create table manufacture(manufacture_id INTEGER PRIMARY KEY,defective_items INTEGER(5),item_name VARCHAR(20),company_name VARCHAR(20),item_color VARCHAR(30),quantity INTEGER(5)')


# creating the goods table
cur.execute('create table goods(goods_id INTEGER(5)PRIMARY KEY,manufactured_date DATE,manufacture_id INTEGER,FOREIGN KEY(manufacture_id) REFERENCES manufacture(manufacture_id)')

# creating purchase table
cur.execute('create table purchase(purchase_id INTEGER(5) PRIMARY KEY,purchase_amt INTEGER,store_name VARCHAR(30),purchase_date DATE)')

# creating sale table
cur.execute('create table sale(sale_id INTEGER(5) PRIMARY KEY,sale_date DATE,profit_margin FLOAT,store_name VARCHAR(30),goods_id INTEGER(5),FOREIGN KEY(goods_id) REFERENCES goods(goods_id))')

#3.Inserting multiple values into manufacture table

i1='insert into manufacture(manufacture_id,defective_items,item_name,company_name,item_color,quantity) values(%s,%s,%s,%s,%s,%s)'
v1=(1,2,'Toy','Toy Vault','red',300),(5,0,'Wooden Chair','century Plyboards','Brown',200),(4,3,'Wooden table','SS Export','Brown',400),(8,4,'Shirt','Hanes','Blue',500)
cur.executemany(i1,v1)
mydb.commit()
print('Data inserted succesfully')

#4.Inserting multiple values in to goods table

i2='insert into goods(goods_id,manufactured_date,manufacture_id) values(%s,%s,%s)'
v2=(10,'2023-04-15',1),(12,'2023-03-13',5),(11,'2024-04-13',4),(14,'2023-04-26',8)
cur.executemany(i2,v2)
mydb.commit()
print('Data inserted succesfully')

#5.Inserting multiple values in to purchase table

i3='insert into purchase(purchase_id,purchase_amt,store_name,purchase_date) values(%s,%s,%s,%s)'
v3=(300,1000,'My Kids','2023-04-19'),(304,2000,'Oray','2023-04-01'),(306,1500,'Discovers','2023-03-12')
cur.executemany(i3,v3)
mydb.commit()
print('Data inserted succesfully')
ss='ALTER table purchase ADD column defective_items INTEGER'
cur.execute(ss)
mydb.commit()
vv='UPDATE purchase SET defective_items=2 where purchase_id=2'
cur.execute(vv)
mydb.commit()
ff='UPDATE purchase SET defective_items=4 where purchase_id=3'
cur.execute(ff)
mydb.commit()
gg='UPDATE purchase SET defective_items=0 where purchase_id=4'
cur.execute(gg)
mydb.commit()


#6.sales table

i4='insert into sale(sale_id,sale_date,profit_margin,store_name,goods_id) values(%s,%s,%s,%s,%s)'
v4=(20,'2023-04-01',200,'My Kids',10),(22,'2023-04-23',100,'Oray',12),(24,'2023-04-22',50,'My Care',11),(28,'2023-04-02',150,'Reliance Mart',14)
cur.executemany(i4,v4)
mydb.commit()
print('Data inserted succesfully')
ss='ALTER table sale ADD column company varchar(30),Add column item_name'
cur.execute(ss)
mydb.commit()
vv='UPDATE sale SET company="SS Export",item_name="Wooden table" where goods_id=10'
cur.execute(vv)
mydb.commit()
va='UPDATE sale SET company="Toy Vault",item_name="Toy" where goods_id=12'
cur.execute(va)
mydb.commit()
vs='UPDATE sale SET company="Century Plyboards",item_name="Wooden Chair" where goods_id=11'
cur.execute(vs)
mydb.commit()
vb='UPDATE sale SET company="Hanes",item_name="Shirt" where goods_id=14'
cur.execute(vb)
mydb.commit()

#Queries
#7.
a='DELETE FROM purchase WHERE defective_items=4 AND purchase_date="2023-04-01" AND store_name="Oray"'
cur.execute(a)
mydb.commit()

#8.
b='UPDATE manufacture SET quantity=100 WHERE item_color="red" AND manufacture_id IN (SELECT manufacture_id FROM goods WHERE goods_id IN (SELECT goods_id FROM sale WHERE store_name="My Kids"))'
cur.execute(b)
mydb.commit()

#9.
d='SELECT * FROM goods JOIN manufacture ON goods.manufacture_id=manufacture.manufacture_id WHERE item_name="Wooden Chair" AND manufactured_date < "2023-05-01"'
cur.execute(d)
r=cur.fetchall()
for i in r:
    print(i)
mydb.commit()

#10.
s='SELECT sale.profit_margin FROM sale JOIN goods on sale.goods_id=goods.goods_id JOIN manufacture ON goods.manufacture_id=manufacture.manufacture_id  WHERE sale.item_name="Wooden table" AND store_name="My Care" AND company="SS Export"'
cur.execute(s)
r=cur.fetchone()
print(r[0])
mydb.commit()

