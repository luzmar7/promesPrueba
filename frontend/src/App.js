/*import React, { Component } from 'react';

class App extends Component {
  state = {
    medicos: []
  };

  async componentDidMount() {
    try {
      const respuesta = await fetch('http://127.0.0.1:8000/v1/medicos/');
      const medicos = await respuesta.json();
      this.setState({
        medicos
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div>
        {this.state.medicos.map(item => (
          <div key={item.id}>
            <h1>{item.nombre_m}</h1>
            <span>{item.apellido_m}</span>
          </div>
        ))}
      </div>
    );
  }
} 

export default App; */



import React, { Component } from 'react';

var url = 'http://127.0.0.1:8000/v1/generar/1/';

class App extends Component {
  constructor(props) {
    super(props)

    this.state = {
      fecha: '',
      examen: ''
    }

    this.handleOnSubmit = this.handleOnSubmit.bind(this)
}


  handleOnSubmit(e) {
    e.preventDefault()

    let data = {
      fecha: this.state.fecha.value,
      examen: this.state.examen.value
    }

    try {

      fetch(url, {
        method: 'POST', // or 'PUT'
        body: JSON.stringify(data), // data can be string or {object}!
        headers:{
          'Content-Type': 'application/json'
        }
      }).then(res => res.json())
      .catch(error => console.error('Error:', error))
      .then(response => console.log('Success:', response));

    } catch (e) {
      console.log(e);
    }
   
  }

  render() {
    return (
      <div>
        <h1>Registro de Ordenes</h1>
        <form  onSubmit={this.handleOnSubmit} method="POST">
          <input type="text" placeholder="FECHA" ref={fecha => this.state.fecha = fecha}/>
          <input type="text" placeholder="Cantidad de habitantes" ref={examen => this.state.examen = examen}/>
          
          <input type="submit" value="Registrar" />
        </form>
      </div>
    );
  }
}

export default App;
