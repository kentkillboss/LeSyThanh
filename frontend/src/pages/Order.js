import React, { Component } from 'react';
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faEdit, faTrashAlt } from '@fortawesome/free-solid-svg-icons';
import { Modal, ModalBody, ModalFooter, ModalHeader } from 'reactstrap';
import { AvForm, AvField } from 'availity-reactstrap-validation';

const url="http://192.168.1.7:8080/order/all";
const urldelete = "http://192.168.1.7:8080/order/delete/";
const urlupdate = "http://192.168.1.7:8080/order/update/";
const urladd = "http://192.168.1.7:8080/order/insert";

class App extends Component {
state={
  data:[],
  handleinsert: false,
  handledelete: false,
  form:{
    OrderID: '',
    CustomerID: '',
    EmployeeID: '',
    OrderDate: '',
    ShipperID: '',
    cc: ''
  }
}

onSubmit(e){
  e.preventDefault();
  this.form.validateAll();

  if ( this.checkBtn.context._errors.length === 0 ) {
     alert('success');
  }
}

handleget=()=>{
axios.get(url).then(response=>{
  this.setState({data: response.data});
}).catch(error=>{
  console.log(error.message);
})
}

handlepost=async()=>{
  delete this.state.form.OrderID;
 await axios.post(urladd,this.state.form).then(response=>{
    this.handleinsert();
    this.handleget();
  }).catch(error=>{
    console.log(error.message);
  })
}

handleput=()=>{
  axios.put(urlupdate+this.state.form.OrderID, this.state.form).then(response=>{
    this.handleinsert();
    this.handleget();
  })
}

handledelete=()=>{
  axios.delete(urldelete+this.state.form.OrderID).then(response=>{
    this.setState({handledelete: false});
    this.handleget();
  })
}

handleinsert=()=>{
  this.setState({handleinsert: !this.state.handleinsert});
}

selectedItem=(item)=>{
  this.setState({
    cc: 'update',
    form: {
      OrderID: item.OrderID,
      CustomerID: item.CustomerID,
      EmployeeID: item.EmployeeID,
      OrderDate: item.OrderDate,
      ShipperID: item.ShipperID,
    }
  })
}

handleChange=async e=>{
e.persist();
await this.setState({
  form:{
    ...this.state.form,
    [e.target.name]: e.target.value
  }
});
console.log(this.state.form);
}

  componentDidMount() {
    this.handleget();
  }
  

  render(){
    const {form}=this.state;
  return (
    <div className="App">
    <br /><br /><br />
  <button className="btn btn-success" onClick={()=>{this.setState({form: null, cc: 'insert'}); this.handleinsert()}}>Thêm</button>
  <br /><br />
    <table className="table ">
      <thead>
        <tr>
          <th>ID</th>
          <th>CustomerID</th>
          <th>EmployeeID</th>
          <th>OrderDate</th>
          <th>ShipperID</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        {this.state.data.map(item=>{
          return(
            <tr>
          <td>{item.OrderID}</td>
          <td>{item.CustomerID}</td>
          <td>{item.EmployeeID}</td>
          <td>{item.OrderDate}</td>
          <td>{item.ShipperID}</td>
          <td>
                <button className="btn btn-primary" onClick={()=>{this.selectedItem(item); this.handleinsert()}}><FontAwesomeIcon icon={faEdit}/></button>
                {"   "}
                <button className="btn btn-danger" onClick={()=>{this.selectedItem(item); this.setState({handledelete: true})}}><FontAwesomeIcon icon={faTrashAlt}/></button>
                </td>
          </tr>
          )
        })}
      </tbody>
    </table>



    <Modal isOpen={this.state.handleinsert}>
                <ModalHeader style={{display: 'block'}}>
                {this.state.cc==='insert'?
                  <span>Nhập thông tin</span>:
                  <span>Sửa thông tin</span>
                }
                  <span style={{float: 'right'}} onClick={()=>this.handleinsert()}>x</span>
                </ModalHeader>
                <ModalBody>
                <div>
                    <AvForm >
                        <AvField name="CustomerID" label="CustomerID" type="text" onChange={this.handleChange} value={form?form.CustomerID: '' } placeholder = "Chỉ nhập số" required />
                        <AvField name="EmployeeID" label="EmployeeID" type="text" onChange={this.handleChange} value={form?form.EmployeeID: '' } placeholder = "Chỉ nhập số" required />
                        <AvField name="OrderDate" label="OrderDate" type="text" onChange={this.handleChange} value={form?form.OrderDate: '' } placeholder = "x/x/xxxx" required />
                        <AvField name="ShipperID" label="ShipperID" type="text" onChange={this.handleChange} value={form?form.ShipperID: '' } placeholder = "Chỉ nhập số" required />
                    </AvForm>
                </div>
                </ModalBody>

                <ModalFooter>
                  {this.state.cc==='insert'?
                    <button className="btn btn-success" onClick={()=>this.handlepost()}>
                    Thêm
                  </button>: <button className="btn btn-primary" onClick={()=>this.handleput()}>
                    Sửa
                  </button>
  }
                    <button className="btn btn-danger" onClick={()=>this.handleinsert()}>Hủy</button>
                </ModalFooter>
          </Modal>


          <Modal isOpen={this.state.handledelete}>
            <ModalBody>
               Bạn có muốn xóa dòng này {form && form.a}
            </ModalBody>
            <ModalFooter>
              <button className="btn btn-danger" onClick={()=>this.handledelete()}>Đồng ý</button>
              <button className="btn btn-secundary" onClick={()=>this.setState({handledelete: false})}>Hủy</button>
            </ModalFooter>
          </Modal>
  </div>
  );
}

}

export default App;