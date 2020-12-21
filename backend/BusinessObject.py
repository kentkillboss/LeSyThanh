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
    def __init__(self, CategoryID=None, CategoryName=None, Description=None):
        self.CategoryID = CategoryID
        self.CategoryName = CategoryName
        self.Description = Description

    def fetch_data(self, data):
        self.CategoryID = data[0]
        self.CategoryName = data[1]
        self.Description = data[2]

    def to_json(self):
        return {
            'CategoryID': self.CategoryID,
            'CategoryName': self.CategoryName,
            'Description': self.Description
        }

class Order:
    def __init__(self, OrderID=None, CustomerID=None, EmployeeID=None, OrderDate=None, ShipperID=None, Details=[]):
        self.OrderID = OrderID
        self.CustomerID = CustomerID
        self.EmployeeID = EmployeeID
        self.OrderDate = OrderDate
        self.ShipperID = ShipperID
        self.Details = Details

    def fetch_data(self, data):
        self.OrderID = data[0]
        self.OrderDate = data[3]
        self.customer = Customer()
        self.customer.fetch_data(data[5:12])
        self.employee = Employee()
        self.employee.fetch_data(data[12:18])
        self.shipper = Shipper()
        self.shipper.fetch_data(data[18:21])

    def to_json(self):
        return {
            'OrderID': self.OrderID,
            'OrderDate': self.OrderDate,
            'customer': self.customer.to_json(),
            'employee': self.employee.to_json(),
            'shipper': self.shipper.to_json(),
            'Details': self.Details
        }

class OrderDetail:
    def __init__(self, OrderDetailID=None, OrderID=None, ProductID=None, Quantity=None):
        self.OrderDetailID = OrderDetailID
        self.OrderID = OrderID
        self.ProductID = ProductID
        self.Quantity = Quantity

    def fetch_data(self, data):
        self.OrderDetailID = data[0]
        self.OrderID = data[1]
        self.ProductID = data[2]
        self.Quantity = data[3]

    def to_json(self):
        return {
            'OrderDetailID': self.OrderDetailID,
            'OrderID': self.OrderID,
            'ProductID': self.ProductID,
            'Quantity': self.Quantity
        }

if __name__ == "__main__":
    print('this is business object package')