from flask import Flask
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
    c2 = do.Customer(ConnectionData)
    c1 = bo.Customer(1,'DAU xanh','Peter','566 Nui Thanh', 'Da Nang','5000','VietNam')
    s1 = c2.insert(c1)
    return s1

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)