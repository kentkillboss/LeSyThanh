import React, { Component } from 'react';
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faEdit, faTrashAlt } from '@fortawesome/free-solid-svg-icons';
import { Modal, ModalBody, ModalFooter, ModalHeader } from 'reactstrap';
import { AvForm, AvField } from 'availity-reactstrap-validation';

const url="http://192.168.1.7:8080/order_detail/all";
const urldelete = "http://192.168.1.7:8080/order_detail/delete/";
const urlupdate = "http://192.168.1.7:8080/order_detail/update/";
const urladd = "http://192.168.1.7:8080/order_detail/insert";

class App extends Component {
state={
  data:[],
  handleinsert: false,
  handledelete: false,
  form:{
    OrderDetailID: '',
    OrderID: '',
    ProductID: '',
    Quantity: '',
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
  //delete this.state.form.OrderDetailID;
 await axios.post(urladd,this.state.form).then(response=>{
    this.handleinsert();
    this.handleget();
  }).catch(error=>{
    console.log(error.message);
  })
}

handleput=()=>{
  axios.put(urlupdate+this.state.form.OrderDetailID, this.state.form).then(response=>{
    this.handleinsert();
    this.handleget();
  })
}

handledelete=()=>{
  axios.delete(urldelete+this.state.form.OrderDetailID).then(response=>{
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
      OrderDetailID: item.OrderDetailID,
      OrderID: item.OrderID,
      ProductID: item.ProductID,
      Quantity: item.Quantity,
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
          <th>OrderID</th>
          <th>ProductID</th>
          <th>Quantity</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        {this.state.data.map(item=>{
          return(
            <tr>
          <td>{item.OrderDetailID}</td>
          <td>{item.OrderID}</td>
          <td>{item.ProductID}</td>
          <td>{item.Quantity}</td>
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
                        <AvField name="OrderID" label="OrderID" type="text" onChange={this.handleChange} value={form?form.OrderID: '' } placeholder = "Chỉ nhập số" required />
                        <AvField name="ProductID" label="ProductID" type="text" onChange={this.handleChange} value={form?form.ProductID: '' } placeholder = "Chỉ nhập số" required />
                        <AvField name="Quantity" label="Quantity" type="text" onChange={this.handleChange} value={form?form.Quantity: '' } placeholder = "Chỉ nhập số" required />
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