import sqlite3

conn = sqlite3.connect('ims.db')

cur = conn.cursor()

cur.execute("create table customer(customer_id varchar(30),customer_name varchar(30),customer_addr varchar(30),customer_email varchar(30))")


cur.execute("create table product(product_id,product_name,stock,price,supplier_id)")

cur.execute("create table supplier(supplier_id,supplier_name,supplier_addr,supplier_email)")

cur.execute("create table orders(order_id,product_id,customer_id,quantity)")