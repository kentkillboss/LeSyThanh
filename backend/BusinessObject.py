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

if __name__ == "__main__":
    print('this is business object package')