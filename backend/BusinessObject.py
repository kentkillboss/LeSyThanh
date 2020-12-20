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

if __name__ == "__main__":
    print('this is business object package')