#Queries

import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Sukanya@2003',database='Inventory_Management')
cur=mydb.cursor()
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
