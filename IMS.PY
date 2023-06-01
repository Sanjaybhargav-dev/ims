from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

import pyodbc

server = 'DESKTOP-EAJII0V\SQLEXPRESS'
database = 'newims'
driver = '{SQL Server}'

connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};trusted_connection=yes'

conn = pyodbc.connect(connection_string)



#cn.execute(f"insert into customer(customer_name,customer_addr,customer_email) values('{customer_name}','{customer_addr}','{customer_email}')")
#conn.commit()
@app.route('/')
def home():
    return render_template('index.html')



@app.route('/show-customers')
def customer_show():
    cn = conn.cursor()
    cn.execute("select * from customer")
    data = []
    for i in cn.fetchall():
        customer = {}
        customer['coustomer_id'] = i[0]
        customer['customer_name'] = i[1]
        customer['customer_addr'] = i[2]
        customer['customer_email'] = i[3]
        data.append(customer)


    return render_template('showcustomers.html',data = data)



@app.route('/show-product')
def product_show():
    cn = conn.cursor()
    cn.execute("select * from product")
    data = []
    for i in cn.fetchall():
        product = {}
        product['product_id'] = i[0]
        product['product_name'] = i[1]
        product['product_stock'] = i[2]
        product['product_price'] = i[3]
        product['product_supplierid'] = i[4]
        data.append(product)


    return render_template('showproduct.html',data = data)

@app.route('/add-customer',methods = ['GET','POST'])
def  addcustomer():
     if request.method=='POST':
        cn = conn.cursor()
        customername = request.form.get('name')
        customeraddr = request.form.get('address')
        customeremail = request.form.get('email')
        cn.execute(f"insert into customer(customer_name,customer_addr,customer_email)values('{customername}','{customeraddr}','{customeremail}')")
        conn.commit()
        print('Data has been inserted')
        return jsonify({'message':'sucessfull'})
     else:
         return render_template('addcustomer.html')
     
@app.route('/update-customer',methods = ['GET','POST'])
def updatecustomer():
    if request.method=='POST':
        cn = conn.cursor()
        customerid = request.form.get('customerid')
        change = request.form.get('change')
        newvalue = request.form.get('newvalue')
        cn.execute(f"update customer set {change} = '{newvalue}' where customer_id = '{customerid}'")
        conn.commit()
        print('Data has been updates')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('updatecustomer.html')


@app.route('/update-product' ,methods = ['GET','POST'])   
def updateproduct():
    if request.method=='POST':
        cn = conn.cursor()
        productid = request.form.get("productid")
        change =request.form.get("change")
        newvalue = request.form.get("newvalue")
        cn.execute(f"update product set {change} = '{newvalue}' where product_id = '{productid}'")
        conn.commit()
        print('Data has been updates')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('updateproduct.html')




@app.route('/update-orders' ,methods = ['GET','POST'])   
def updateorders():
    if request.method=='POST':
        cn = conn.cursor()
        orderid = request.form.get("orderid")
        change =request.form.get("change")
        newvalue = request.form.get("newvalue")
        cn.execute(f"update orders set {change} = '{newvalue}' where order_id = '{orderid}'")
        conn.commit()
        print('Data has been updates')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('updateorders.html')


@app.route('/show-orders')
def orders_show():
    cn = conn.cursor()
    cn.execute("select * from orders")
    data = []
    for i in cn.fetchall():
        orders = {}
        orders['order_id'] = i[0]
        orders['product_id'] = i[1]
        orders['customer_id'] = i[2]
        orders['quantity'] = i[3]
        data.append(orders)

    return render_template('showorders.html',data = data)


@app.route('/show-supplier')
def supplier_show():
    cn = conn.cursor()
    cn.execute("select * from supplier")
    data = []
    for i in cn.fetchall():
        supplier = {}
        supplier['supplier_id'] = i[0]
        supplier['supplier_name'] = i[1]
        supplier['supplier_addr'] = i[2]
        supplier['supplier_email'] = i[3]
        data.append(supplier)

    return render_template('showsupplier.html',data = data)


@app.route('/update-suppliers' ,methods = ['GET','POST'])   
def updatesuppliers():
    if request.method=='POST':
        cn = conn.cursor()
        supplierid = request.form.get("supplierid")
        change =request.form.get("change")
        newvalue = request.form.get("newvalue")
        cn.execute(f"update suppliers set {change} = '{newvalue}' where supplier_id = '{supplierid}'")
        conn.commit()
        print('Data has been updates')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('updatesuppliers.html')



if __name__ == '__main__':
    app.run()




