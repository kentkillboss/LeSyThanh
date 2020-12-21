class Customer:
    def __init__(self, CustomerID=None, CustomerName=None, ContactName=None, Address=None, City=None, PostalCode=None, Country=None):
        self.CustomerID = CustomerID
        self.CustomerName = CustomerName
        self.ContactName = ContactName
        self.Address = Address
        self.City = City
        self.PostalCode = PostalCode
        self.Country = Country

    def fetch_data(self,data):
        self.CustomerID = data[0]
        self.CustomerName = data[1]
        self.ContactName = data[2]
        self.Address = data[3]
        self.City = data[4]
        self.PostalCode = data[5]
        self.Country = data[6]
    
    def to_json(self):
        return{
            'CustomerID' : self.CustomerID,
            'CustomerName' : self.CustomerName,
            'ContactName' : self.ContactName,
            'Address' : self.Address,
            'City' : self.City,
            'PostalCode' : self.PostalCode,
            'Country' : self.Country
        }

class Employee:
    def __init__(self, EmployeeID=None, LastName=None, FirstName=None, Birthdate=None, Photo=None, Notes=None):
        self.EmployeeID = EmployeeID
        self.LastName = LastName
        self.FirstName = FirstName
        self.Birthdate = Birthdate
        self.Photo = Photo
        self.Notes = Notes

    def fetch_data(self, data):
        self.EmployeeID = data[0]
        self.LastName = data[1]
        self.FirstName = data[2]
        self.Birthdate = data[3]
        self.Photo = data[4]
        self.Notes = data[5]

    def to_json(self):
        return {
            'EmployeeID': self.EmployeeID,
            'LastName': self.LastName,
            'FirstName': self.FirstName,
            'Birthdate': self.Birthdate,
            'Photo': self.Photo,
            'Notes': self.Notes
        }

class Supplier:
    # Default attributes value are None
    def __init__(self, SupplierID=None, SupplierName=None, ContactName=None, Address=None, City=None, PostalCode=None, Country=None, Phone=None):
        self.SupplierID = SupplierID
        self.SupplierName = SupplierName
        self.ContactName = ContactName
        self.Address = Address
        self.City = City
        self.PostalCode = PostalCode
        self.Country = Country
        self.Phone = Phone

    def fetch_data(self, data):
        self.SupplierID = data[0]
        self.SupplierName = data[1]
        self.ContactName = data[2]
        self.Address = data[3]
        self.City = data[4]
        self.PostalCode = data[5]
        self.Country = data[6]
        self.Phone = data[7]

    def to_json(self):
        return {
            'SupplierID': self.SupplierID,
            'SupplierName': self.SupplierName,
            'ContactName': self.ContactName,
            'Address': self.Address,
            'City': self.City,
            'PostalCode': self.PostalCode,
            'Country': self.Country,
            'Phone': self.Phone
        }

class Category:
    def __init__(self, category_id=None, category_name=None, description=None):
        self.category_id = category_id
        self.category_name = category_name
        self.description = description

    def fetch_data(self, data):
        self.category_id = data[0]
        self.category_name = data[1]
        self.description = data[2]

    def to_json(self):
        return {
            'category_id': self.category_id,
            'category_name': self.category_name,
            'description': self.description
        }

        class Order:
    def __init__(self, order_id=None, customer_id=None, employee_id=None, order_date=None, shipper_id=None, details=[]):
        self.order_id = order_id
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.order_date = order_date
        self.shipper_id = shipper_id
        self.details = details

    def fetch_data(self, data):
        self.order_id = data[0]
        self.order_date = data[3]
        self.customer = Customer()
        self.customer.fetch_data(data[5:12])
        self.employee = Employee()
        self.employee.fetch_data(data[12:18])
        self.shipper = Shipper()
        self.shipper.fetch_data(data[18:21])

    def to_json(self):
        return {
            'order_id': self.order_id,
            'order_date': self.order_date,
            'customer': self.customer.to_json(),
            'employee': self.employee.to_json(),
            'shipper': self.shipper.to_json(),
            'details': self.details
        }

class OrderDetail:
    def __init__(self, order_detail_id=None, order_id=None, product_id=None, quantity=None):
        self.order_detail_id = order_detail_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity

    def fetch_data(self, data):
        self.order_detail_id = data[0]
        self.order_id = data[1]
        self.product_id = data[2]
        self.quantity = data[3]

    def to_json(self):
        return {
            'order_detail_id': self.order_detail_id,
            'order_id': self.order_id,
            'product_id': self.product_id,
            'quantity': self.quantity
        }

if __name__ == "__main__":
    print('this is business object package')