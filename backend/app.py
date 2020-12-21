from flask import Flask, jsonify, request
import os
import BusinessObject as bo
import DataObject as do 

app = Flask(__name__)

db_ip = os.getenv("db_ip")
ConnectionData = {}
ConnectionData['user'] = 'postgres'
ConnectionData['password'] = 'postgres'
ConnectionData['host'] = str(db_ip)
ConnectionData['port'] = '5432'
ConnectionData['database'] = 'northwind'

@app.route("/")
def hello():
   return "hello"
@app.route("/test_insert")
def test_insert():
    c2 = do.Employee(ConnectionData)
    c1 = bo.Employee(1,'Thanh','Le','1999', 'Da Nang','VietNam')
    s1 = c2.insert(c1)
    return s1

@app.route('/test_send_receive', methods=['POST'])
def test_send_receive():
    x = request.json['x']
    y = x + 1
    result = {}
    result['y'] = y
    return jsonify(result), 200

@app.route('/user/insert', methods=['POST'])
def user_insert():
    data = request.json
    c1 = bo.Customer(data['CustomerID'], data['CustomerName'], data['ContactName'], data['Address'], data['City'], data['PostalCode'], data['Country'])
    c2 = do.Customer(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200

@app.route('/user/all')
def get_all_user():
    result = do.Customer(ConnectionData).get_all()
    return jsonify(result), 200

@app.route('/user/get/<int:customer_id>')
def get_user_by_id(customer_id):
    c = bo.Customer(CustomerID=customer_id)
    result = do.Customer(ConnectionData).get_by_id(c)
    if result[1] != 200:
        return jsonify({'message':result[0]}), result[1]
    return jsonify(result[0].to_json()), 200

@app.route('/user/update/<int:customer_id>',methods=['PUT'])
def update_user_by_id(customer_id):
    data = request.json
    c = bo.Customer(CustomerID = customer_id, CustomerName=data['CustomerName'], ContactName=data['ContactName'],Address=data['Address'], City=data['City'], PostalCode=data['PostalCode'], Country=data['Country'])
    result = do.Customer(ConnectionData).update(c)
    return jsonify({'message':result[0]}),result[1]

@app.route('/user/delete/<int:customer_id>', methods=['DELETE'])
def delete_user_by_id(customer_id):
    c = bo.Customer(CustomerID=customer_id)
    result = do.Customer(ConnectionData).delete(c)
    return jsonify({'message':result[0]}), result[1]
    
#Employee
@app.route('/employee/insert', methods=['POST'])
def employee_insert():
    data = request.json
    c1 = bo.Employee(LastName=data['LastName'], FirstName=data['FirstName'], Birthdate=data['Birthdate'], Photo=data['Photo'], Notes=data['Notes'])
    c2 = do.Employee(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200

@app.route('/employee/all')
def get_all_employee():
    result = do.Employee(ConnectionData).get_all()
    return jsonify(result), 200

@app.route('/employee/<int:employee_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_employee(employee_id):
    if request.method == 'GET':
        # Get 
        c = bo.Employee(EmployeeID=employee_id)
        result = do.Employee(ConnectionData).get_by_id(c)
        if result[1] != 200:
            return jsonify({'message': result[0]}), result[1]
        return jsonify(result[0].to_json()), 200
    elif request.method == 'PUT':
        # Update 
        data = request.json
        c = bo.Employee(EmployeeID=employee_id, LastName=data['LastName'], FirstName=data['FirstName'], Birthdate=data['Birthdate'], Photo=data['Photo'], Notes=data['Notes'])
        result = do.Employee(ConnectionData).update(c)
        return jsonify({'message': result[0]}), result[1]
    elif request.method == 'DELETE':
        # Delete 
        c = bo.Employee(EmployeeID=employee_id)
        result = do.Employee(ConnectionData).delete(c)
        return jsonify({'message': result[0]}), result[1]

#Supplier
@app.route('/supplier/insert', methods=['POST'])
def supplier_insert():
    data = request.json
    c1 = bo.Supplier(SupplierName=data['SupplierName'], ContactName=data['ContactName'], Address=data['Address'], City=data['City'], PostalCode=data['PostalCode'], Country=data['Country'], Phone=data['Phone'])
    c2 = do.Supplier(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200

@app.route('/supplier/all')
def get_all_supplier():
    result = do.Supplier(ConnectionData).get_all()
    return jsonify(result), 200

@app.route('/supplier/get/<int:supplier_id>')
def get_supplier_by_id(supplier_id):
    c = bo.Supplier(SupplierID=supplier_id)
    result = do.Supplier(ConnectionData).get_by_id(c)
    if result[1] != 200:
        return jsonify({'message': result[0]}), result[1]
    return jsonify(result[0].to_json()), 200

@app.route('/supplier/update/<int:supplier_id>', methods=['PUT'])
def update_supplier_by_id(supplier_id):
    data = request.json
    c = bo.Supplier(SupplierID=supplier_id, SupplierName=data['SupplierName'], ContactName=data['ContactName'], Address=data['Address'], City=data['City'], PostalCode=data['PostalCode'], Country=data['Country'], Phone=data['Phone'])
    result = do.Supplier(ConnectionData).update(c)
    return jsonify({'message': result[0]}), result[1]

@app.route('/supplier/delete/<int:supplier_id>', methods=['DELETE'])
def delete_supplier_by_id(supplier_id):
    c = bo.Supplier(SupplierID=supplier_id)
    result = do.Supplier(ConnectionData).delete(c)
    return jsonify({'message': result[0]}), result[1]

#category
@app.route('/category/all')
def get_all_category():
    c = do.Category(ConnectionData).get_all()
    return jsonify(c), 200

@app.route('/category/insert', methods=['POST'])
def insert_category():
    data = request.json
    category = bo.Category(CategoryName=data['category_name'], Description=data['description'])
    result = do.Category(ConnectionData).insert(category)
    return jsonify({'message': result}), 200

@app.route('/category/get/<int:category_id>')
def get_category_by_id(category_id):
    category = bo.Category(CategoryID=category_id)
    result = do.Category(ConnectionData).get_by_id(category)
    if result[1] != 200:
        return jsonify({'message': result[0]}), result[1]
    return jsonify(result[0].to_json()), 200

@app.route('/category/update/<int:category_id>', methods=['PUT'])
def update_category_by_id(category_id):
    data = request.json
    category = bo.Category(CategoryID=category_id, CategoryName=data['category_name'], Description=data['description'])
    result = do.Category(ConnectionData).update(category)
    return jsonify({'message': result[0]}), result[1]

@app.route('/category/delete/<int:category_id>', methods=['DELETE'])
def delete_category_by_id(category_id):
    c = bo.Category(CategoryID=category_id)
    result = do.Category(ConnectionData).delete(c)
    return jsonify({'message': result[0]}), result[1]

#order
@app.route('/order/insert', methods=['POST'])
def order_insert():
    data = request.json
    c1 = bo.Order(customer_id=data['customer_id'], employee_id=data['employee_id'], order_date=data['order_date'], shipper_id=data['shipper_id'])
    c2 = do.Order(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200

@app.route('/order/all')
def get_all_order():
    result = do.Order(ConnectionData).get_all()
    return jsonify(result), 200

@app.route('/order/<int:order_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_order(order_id):
    if request.method == 'GET':
        c = bo.Order(order_id=order_id)
        result = do.Order(ConnectionData).get_by_id(c)
        if result[1] != 200:
            return jsonify({'message': result[0]}), result[1]
        return jsonify(result[0].to_json()), 200
    elif request.method == 'PUT':
        data = request.json
        c = bo.Order(order_id=order_id, customer_id=data['customer_id'], employee_id=data['employee_id'], order_date=data['order_date'], shipper_id=data['shipper_id'])
        result = do.Order(ConnectionData).update(c)
        return jsonify({'message': result[0]}), result[1]
    elif request.method == 'DELETE':
        c = bo.Order(order_id=order_id)
        result = do.Order(ConnectionData).delete(c)
        return jsonify({'message': result[0]}), result[1]

#ortherdetail
@app.route('/order_detail/insert', methods=['POST'])
def order_detail_insert():
    data = request.json
    c1 = bo.OrderDetail(order_id=data['order_id'], product_id=data['product_id'], quantity=data['quantity'])
    c2 = do.OrderDetail(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200

@app.route('/order_detail/all')
def get_all_order_detail():
    result = do.OrderDetail(ConnectionData).get_all()
    return jsonify(result), 200

@app.route('/order_detail/<int:order_detail_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_order_detail(order_detail_id):
    if request.method == 'GET':
        c = bo.OrderDetail(order_detail_id=order_detail_id)
        result = do.OrderDetail(ConnectionData).get_by_id(c)
        if result[1] != 200:
            return jsonify({'message': result[0]}), result[1]
        return jsonify(result[0].to_json()), 200
    elif request.method == 'PUT':
        data = request.json
        c = bo.OrderDetail(order_detail_id=order_detail_id, order_id=data['order_id'], product_id=data['product_id'], quantity=data['quantity'])
        result = do.OrderDetail(ConnectionData).update(c)
        return jsonify({'message': result[0]}), result[1]
    elif request.method == 'DELETE':
        c = bo.OrderDetail(order_detail_id=order_detail_id)
        result = do.OrderDetail(ConnectionData).delete(c)
        return jsonify({'message': result[0]}), result[1]

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)