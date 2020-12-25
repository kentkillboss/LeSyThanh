import psycopg2
from BusinessObject import Customer as CustomerEntity
from BusinessObject import Employee as EmployeeEntity
from BusinessObject import Supplier as SupplierEntity
from BusinessObject import Category as CategoryEntity
from BusinessObject import Order as OrderEntity
from BusinessObject import OrderDetail as OrderDetailEntity
from BusinessObject import Product as ProductEntity
from BusinessObject import Shipper as ShipperEntity

class Customer:
    def __init__(self,ConnectionData):
        self.ConnectionData = ConnectionData
    def insert(self,customer):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO TblCustomers(CustomerName,ContactName,Address,City,PostalCode,Country) VALUES (%s,%s,%s,%s,%s,%s)"
            record_to_insert = (customer.CustomerName,customer.ContactName,customer.Address,customer.City,customer.PostalCode,customer.Country)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert TblCustomers successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM TblCustomers"
            cur.execute(sql)
            con.commit()           
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = CustomerEntity()
                c.fetch_data(row)
                result.append(c.to_json())
            con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_by_id(self,customer: CustomerEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM TblCustomers WHERE customerid=%s"

            cur.execute(sql,(customer.CustomerID, ))
            con.commit()           
            row = cur.fetchone()
            if row:
                c = CustomerEntity()
                c.fetch_data(row)
                return c, 200
            con.close()
            return "Customer ID not found", 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self, customer: CustomerEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE TblCustomers SET customername=%s,contactname=%s, address=%s,city=%s, postalcode=%s, country=%s WHERE customerid=%s"
            cur.execute(sql,(customer.CustomerName, customer.ContactName, customer.Address, customer.City, customer.PostalCode, customer.Country, customer.CustomerID))
            con.commit()           
            row = cur.rowcount
            if row>0:
                return "Updated Customer", 200
            con.close()
            return "Customer ID not found", 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def delete(self, customer: CustomerEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM TblCustomers WHERE customerid=%s"
            cur.execute(sql,(customer.CustomerID,))
            con.commit()           
            row = cur.rowcount
            if row>0:
                return "Delete Customer", 200
            con.close()
            return "Customer ID not found", 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

class Employee:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData

    def insert(self, employee: EmployeeEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO tblemployees(lastname, firstname, birthdate, photo, notes) VALUES (%s, %s, %s, %s, %s)"
            record_to_insert = (employee.LastName, employee.FirstName, employee.Birthdate, employee.Photo, employee.Notes)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert tblemployees successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM tblemployees"
            cur.execute(sql)
            con.commit()
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = EmployeeEntity()
                c.fetch_data(row)            
                result.append(c.to_json())
            con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_by_id(self, employee: EmployeeEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM tblemployees WHERE employeeid=%s"
            cur.execute(sql, (employee.EmployeeID, ))
            con.commit()
            row = cur.fetchone()
            if row:
                c = EmployeeEntity()
                c.fetch_data(row)
                return c, 200
            con.close()
            return 'Employee ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self, employee: EmployeeEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE tblemployees SET lastname=%s, firstname=%s, birthdate=%s, photo=%s, notes=%s WHERE employeeid=%s"
            cur.execute(sql, (employee.LastName, employee.FirstName, employee.Birthdate, employee.Photo, employee.Notes, employee.EmployeeID))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Updated employee', 200
            con.close()
            return 'Employee ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def delete(self, employee: EmployeeEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM tblemployees WHERE employeeid=%s"
            cur.execute(sql, (employee.EmployeeID, ))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Deleted employee', 200
            con.close()
            return 'Employee ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

class Supplier:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData
    def insert(self, supplier):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO tblsuppliers(Suppliername, ContactName, Address, City, PostalCode, Country, Phone) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            record_to_insert = (supplier.SupplierName, supplier.ContactName, supplier.Address, supplier.City, supplier.PostalCode, supplier.Country, supplier.Phone)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert tblsuppliers successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM tblsuppliers"
            cur.execute(sql)
            con.commit()
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = SupplierEntity()
                c.fetch_data(row)            
                result.append(c.to_json())
            con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_by_id(self, supplier: SupplierEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM tblsuppliers WHERE supplierid=%s"
            cur.execute(sql, (supplier.SupplierID, ))
            con.commit()
            row = cur.fetchone()
            if row:
                c = SupplierEntity()
                c.fetch_data(row)
                return c, 200
            con.close()
            return 'Supplier ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self, supplier: SupplierEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE tblsuppliers SET suppliername=%s, contactname=%s, address=%s, city=%s, postalcode=%s, country=%s, phone=%s WHERE supplierid=%s"
            cur.execute(sql, (supplier.SupplierName, supplier.ContactName, supplier.Address, supplier.City, supplier.PostalCode, supplier.Country, supplier.Phone, supplier.SupplierID))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Updated supplier', 200
            con.close()
            return 'Supplier ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def delete(self, supplier: SupplierEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM tblsuppliers WHERE supplierid=%s"
            cur.execute(sql, (supplier.SupplierID, ))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Deleted supplier', 200
            con.close()
            return 'Supplier ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()
class Category:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData

    def insert(self, category: CategoryEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO tblcategories(categoryname, description) VALUES (%s, %s)"
            record_to_insert = (category.CategoryName, category.Description)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert tblcategories successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM tblcategories"
            cur.execute(sql)
            con.commit()
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = CategoryEntity()
                c.fetch_data(row)            
                result.append(c.to_json())
            con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_by_id(self, category: CategoryEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM tblcategories WHERE categoryid=%s"
            cur.execute(sql, (category.CategoryID, ))
            con.commit()
            row = cur.fetchone()
            if row:
                c = CategoryEntity()
                c.fetch_data(row)
                return c, 200
            con.close()
            return 'Category ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self, category: CategoryEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE tblcategories SET categoryname=%s, description=%s WHERE categoryid=%s"
            cur.execute(sql, (category.CategoryName, category.Description, category.CategoryID))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Updated category', 200
            con.close()
            return 'Category ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def delete(self, category: CategoryEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM tblcategories WHERE categoryid=%s"
            cur.execute(sql, (category.CategoryID, ))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Deleted category', 200
            con.close()
            return 'Category ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

class Order:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData

    def insert(self, order: OrderEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO tblorders(customerid, employeeid, orderdate, shipperid) VALUES (%s, %s, %s, %s)"
            record_to_insert = (order.CustomerID, order.EmployeeID, order.OrderDate, order.ShipperID)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert tblorders successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM tblorders"
            cur.execute(sql)
            con.commit()
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = OrderEntity()
                c.fetch_data(row)            
                result.append(c.to_json())
            con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_by_id(self, order: OrderEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM tblorders WHERE orderid=%s"
            cur.execute(sql, (order.OrderID, ))
            con.commit()
            row = cur.fetchone()
            if row:
                c = OrderEntity()
                c.fetch_data(row)
                return c, 200
            con.close()
            return 'order ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self, order: OrderEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE tblorders SET customerid=%s, employeeid=%s, orderdate=%s, shipperid=%s WHERE orderid=%s"
            cur.execute(sql, (order.CustomerID, order.EmployeeID, order.OrderDate, order.ShipperID, order.OrderID))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Updated order', 200
            con.close()
            return 'order ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def delete(self, order: OrderEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM tblorders WHERE orderid=%s"
            cur.execute(sql, (order.OrderID, ))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Deleted order', 200
            con.close()
            return 'order ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

class OrderDetail:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData

    def insert(self, orderr: OrderDetailEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO tblorderdetails(orderid, productid, quantity) VALUES (%s, %s, %s)"
            record_to_insert = (orderr.OrderID, orderr.ProductID, orderr.Quantity)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert tblorderdetails successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM tblorderdetails"
            cur.execute(sql)
            con.commit()
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = OrderDetailEntity()
                c.fetch_data(row)            
                result.append(c.to_json())
            con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_by_id(self, orderr: OrderDetailEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM tblorderdetails WHERE orderdetailid=%s"
            cur.execute(sql, (orderr.OrderDetailID, ))
            con.commit()
            row = cur.fetchone()
            if row:
                c = OrderDetailEntity()
                c.fetch_data(row)
                return c, 200
            con.close()
            return 'order detail ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self, orderr: OrderDetailEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE tblorderdetails SET orderid=%s, productid=%s, quantity=%s WHERE orderdetailid=%s"
            cur.execute(sql, (orderr.OrderID, orderr.ProductID, orderr.Quantity, orderr.OrderDetailID))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Updated order', 200
            con.close()
            return 'order detail ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def delete(self, orderr: OrderDetailEntity):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM tblorderdetails WHERE orderdetailid=%s"
            cur.execute(sql, (orderr.OrderDetailID, ))
            con.commit()
            row = cur.rowcount
            if row > 0:
                return 'Deleted order detail', 200
            con.close()
            return 'order detail ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

class Product:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData
    def insert(self, product):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO tblproducts(ProductName, SupplierID, CategoryID, Unit, Price) VALUES (%s, %s, %s, %s, %s)"
            record_to_insert = (product.ProductName, product.SupplierID, product.CategoryID, product.Unit, product.Price)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert TblProducts successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM tblproducts"
            cur.execute(sql)
            con.commit()           
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = ProductEntity()
                c.fetch_data(row)
                result.append(c.to_json())
            con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_by_id(self, product: ProductEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM tblproducts WHERE productid=%s"
            cur.execute(sql, (product.ProductID,))
            con.commit()           
            row = cur.fetchone()
            if row:
                c = ProductEntity()
                c.fetch_data(row)
                return c, 200
            con.close()
            return 'Product ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self, product: ProductEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE tblproducts SET productname=%s, supplierid=%s, categoryid=%s, unit=%s, price=%s WHERE productid=%s "
            cur.execute(sql,(product.ProductName, product.SupplierID, product.CategoryID, product.Unit, product.Price, product.ProductID))
            con.commit()           
            row = cur.rowcount
            if row > 0:
                return 'Updated product', 200
            con.close()
            return 'Product ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def delete(self, product: ProductEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM tblproducts WHERE productid=%s"
            cur.execute(sql,(product.ProductID,))
            con.commit()           
            row = cur.rowcount
            if row>0:
                return "Delete Product", 200
            con.close()
            return "Product ID not found", 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

class Shipper:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData
    def insert(self, shipper):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO tblshippers(ShipperID, ShipperName, Phone) VALUES (%s, %s, %s)"
            record_to_insert = (shipper.ShipperID, shipper.ShipperName, shipper.Phone)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert TblShippers successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_all(self):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM tblshippers"
            cur.execute(sql)
            con.commit()           
            rows = cur.fetchall()
            result = []
            for row in rows:
                c = ShipperEntity()
                c.fetch_data(row)
                result.append(c.to_json())
            con.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def get_by_id(self, shipper: ShipperEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "SELECT * FROM tblshippers WHERE shipperid=%s"
            cur.execute(sql, (shipper.ShipperID,))
            con.commit()           
            row = cur.fetchone()
            if row:
                c = ShipperEntity()
                c.fetch_data(row)
                return c, 200
            con.close()
            return 'Shipper ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update(self, shipper: ShipperEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE tblshippers SET shippername=%s, phone=%s WHERE shipperid=%s "
            cur.execute(sql,(shipper.ShipperName, shipper.Phone, shipper.ShipperID))
            con.commit()           
            row = cur.rowcount
            if row > 0:
                return 'Updated shipper', 200
            con.close()
            return 'Shipper ID not found', 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def delete(self, shipper: ShipperEntity):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                password = self.ConnectionData['password'],
                                host = self.ConnectionData['host'],
                                port = self.ConnectionData['port'],
                                database = self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM tblshippers WHERE shipperid=%s"
            cur.execute(sql,(shipper.ShipperID,))
            con.commit()           
            row = cur.rowcount
            if row>0:
                return "Delete Shipper", 200
            con.close()
            return "Shipper ID not found", 404
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

if __name__ == "__main__":
    print('this is data object package')