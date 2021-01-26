import React from 'react';
import './App.css';
import Navbar from './components/NavBar';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Customer from './pages/Customer';
import Category from './pages/Category';
import Employee from './pages/Employee';
import Home from './pages/Home';
import Supplier from './pages/Supplier';
import Product from './pages/Product';
import Order from './pages/Order';
import OrderDetail from './pages/OrderDetail';
import Shipper from './pages/Shipper';
import Footer from "./components/Footer";

function App() {
  return (
    <>
    <div className="page-container">
      <div className="content-wrap">
      <Router>
        <Navbar />
        <Switch>
          <Route path='/' exact component={Home} />
          <Route path='/customer'  component={Customer} />
          <Route path='/category' component={Category} />
          <Route path='/employee' component={Employee} />
          <Route path='/supplier' component={Supplier} />
          <Route path='/product' component={Product} />
          <Route path='/order' component={Order} />
          <Route path='/orderdetail' component={OrderDetail} />
          <Route path='/shipper' component={Shipper} />
        </Switch>
      </Router>
      </div>
      <Footer />
    </div>
    </>
  );
}

export default App;