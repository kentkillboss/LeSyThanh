import React, { Component } from 'react';
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faEdit, faTrashAlt } from '@fortawesome/free-solid-svg-icons';
import { AvForm, AvField } from 'availity-reactstrap-validation';
import {  Button,Modal, ModalBody, ModalFooter, ModalHeader } from 'reactstrap';

const url="http://192.168.1.7:8080/category/all";
const urldelete = "http://192.168.1.7:8080/category/delete/";
const urlupdate = "http://192.168.1.7:8080/category/update/";
const urladd = "http://192.168.1.7:8080/category/insert";

class App extends Component {
state={
  data:[],
  handleinsert: false,
  handledelete: false,
  form:{
    CategoryID: '',
    CategoryName: '',
    Description: '',
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
  //delete this.state.form.CategoryID;
 await axios.post(urladd,this.state.form).then(response=>{
    this.handleinsert();
    this.handleget();
  }).catch(error=>{
    console.log(error.message);
  })
}

handleput=()=>{
  axios.put(urlupdate+this.state.form.CategoryID, this.state.form).then(response=>{
    this.handleinsert();
    this.handleget();
  })
}

handledelete=()=>{
  axios.delete(urldelete+this.state.form.CategoryID).then(response=>{
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
        CategoryID: item.CategoryID,
        CategoryName: item.CategoryName,
        Description: item.Description
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
//console.log(e.target.value);
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
          <th>CategoryName</th>
          <th>Description</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        {this.state.data.map(item=>{
          return(
            <tr>
          <td>{item.CategoryID}</td>
          <td>{item.CategoryName}</td>
          <td>{item.Description}</td>
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
                        <AvField name="CategoryName" label="CategoryName" type="text" onChange={this.handleChange} value={form?form.CategoryName: '' } required />
                        <AvField name="Description" label="Description" type="text" onChange={this.handleChange} value={form?form.Description: '' } required />
                    </AvForm>
                   
                 </div>
                  {/* <div className="form-group">
                    <label htmlFor="id">ID</label>
                    <input className="form-control" type="text" name="CustomerID" id="id" readOnly onChange={this.handleChange} value={form?form.CategoryID: this.state.data.length+1}/>
                    <br />
                    <label htmlFor="a">CategoryName</label>
                    <input   className="form-control" type="text" name="CategoryName" id="CategoryName" onChange={this.handleChange} value={form?form.CategoryName: ''} required />
                    <br />
                    <label htmlFor="a">Description</label>
                    <input   className="form-control" type="text" name="Description" id="Description" onChange={this.handleChange} value={form?form.Description: '' } required />
                    <br />
                  </div> */}
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