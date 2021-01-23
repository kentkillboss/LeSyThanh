import React, { Component } from 'react';
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faEdit, faTrashAlt } from '@fortawesome/free-solid-svg-icons';
import { Modal, ModalBody, ModalFooter, ModalHeader } from 'reactstrap';

const url="http://192.168.1.6:8080/user/all";
const urldelete = "http://192.168.1.6:8080/user/delete/";
const urlupdate = "http://192.168.1.6:8080/user/update/";
const urladd = "http://192.168.1.6:8080/user/insert";

class App extends Component {
state={
  data:[],
  handleinsert: false,
  handledelete: false,
  form:{
    CustomerID: '',
    CustomerName: '',
    ContactName: '',
    Address: '',
    City: '',
    PostalCode: '',
    Country: '',
    cc: ''
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
  delete this.state.form.CustomerID;
 await axios.post(urladd,this.state.form).then(response=>{
    this.handleinsert();
    this.handleget();
  }).catch(error=>{
    console.log(error.message);
  })
}

handleput=()=>{
  axios.put(urlupdate+this.state.form.CustomerID, this.state.form).then(response=>{
    this.handleinsert();
    this.handleget();
  })
}

handledelete=()=>{
  axios.delete(urldelete+this.state.form.CustomerID).then(response=>{
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
      CustomerID: item.CustomerID,
      CustomerName: item.CustomerName,
      ContactName: item.ContactName,
      Address: item.Address,
      City: item.City,
      PostalCode: item.PostalCode,
      Country: item.Country
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
          <th>CustomerName</th>
          <th>ContactName</th>
          <th>Address</th>
          <th>City</th>
          <th>PostalCode</th>
          <th>Country</th>
        </tr>
      </thead>
      <tbody>
        {this.state.data.map(item=>{
          return(
            <tr>
          <td>{item.CustomerID}</td>
          <td>{item.CustomerName}</td>
          <td>{item.ContactName}</td>
          <td>{item.Address}</td>
          <td>{item.City}</td>
          <td>{item.PostalCode}</td>
          <td>{item.Country}</td>
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
                  <span style={{float: 'right'}} onClick={()=>this.handleinsert()}>x</span>
                </ModalHeader>
                <ModalBody>
                  <div className="form-group">
                    <label htmlFor="id">ID</label>
                    <input className="form-control" type="text" name="CustomerID" id="id" readOnly onChange={this.handleChange} value={form?form.CustomerID: this.state.data.length+1}/>
                    <br />
                    <label htmlFor="a">CustomerName</label>
                    <input className="form-control" type="text" name="CustomerName" id="CustomerName" onChange={this.handleChange} value={form?form.CustomerName: ''}/>
                    <br />
                    <label htmlFor="a">ContactName</label>
                    <input className="form-control" type="text" name="ContactName" id="ContactName" onChange={this.handleChange} value={form?form.ContactName: ''}/>
                    <br />
                    <label htmlFor="a">Address</label>
                    <input className="form-control" type="text" name="Address" id="Address" onChange={this.handleChange} value={form?form.Address: ''}/>
                    <br />
                    <label htmlFor="a">City</label>
                    <input className="form-control" type="text" name="City" id="City" onChange={this.handleChange} value={form?form.City: ''}/>
                    <br />
                    <label htmlFor="a">PostalCode</label>
                    <input className="form-control" type="text" name="PostalCode" id="PostalCode" onChange={this.handleChange} value={form?form.PostalCode: ''}/>
                    <br />
                    <label htmlFor="a">Country</label>
                    <input className="form-control" type="text" name="Country" id="Country" onChange={this.handleChange} value={form?form.Country: ''}/>
                    <br />
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