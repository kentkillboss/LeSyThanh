import psycopg2
from BusinessObject import Customer as CustomerEntity
from BusinessObject import Employee as EmployeeEntity
from BusinessObject import Supplier as SupplierEntity
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
if __name__ == "__main__":
    print('this is data object package')