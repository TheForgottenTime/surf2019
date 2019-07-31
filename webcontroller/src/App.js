import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";
import Button from "@material-ui/core/Button";
const axios = require("axios");
class App extends Component {
  constructor(props) {
    super(props);
    this.escFunction = this.escFunction.bind(this);
  }
  escFunction(event) {
    switch (event.keyCode) {
      case 27:
        console.log("Escape");
        axios
          .get("http://localhost:3000/brake")
          .then(function(response) {
            // handle success
            console.log(response);
          })
          .catch(function(error) {
            // handle error
            console.log(error);
          });
        break;
      case 87:
        console.log("W");
        axios
          .get("http://localhost:3000/goForward")
          .then(function(response) {
            // handle success
            console.log(response);
          })
          .catch(function(error) {
            // handle error
            console.log(error);
          });
        break;
      case 65:
        console.log("A");
        axios
          .get("http://localhost:3000/turnLeft")
          .then(function(response) {
            // handle success
            console.log(response);
          })
          .catch(function(error) {
            // handle error
            console.log(error);
          });
        break;
      case 83:
        console.log("S");
        axios
          .get("http://localhost:3000/goBackward")
          .then(function(response) {
            // handle success
            console.log(response);
          })
          .catch(function(error) {
            // handle error
            console.log(error);
          });
        break;
      case 68:
        console.log("D");
        axios
          .get("http://localhost:3000/turnRight")
          .then(function(response) {
            // handle success
            console.log(response);
          })
          .catch(function(error) {
            // handle error
            console.log(error);
          });
        break;
      case 16:
        console.log("Shift");
        axios
          .get("http://localhost:3000/goUp")
          .then(function(response) {
            // handle success
            console.log(response);
          })
          .catch(function(error) {
            // handle error
            console.log(error);
          });
        break;
      case 17:
        console.log("Ctrl");
        axios
          .get("http://localhost:3000/goDown")
          .then(function(response) {
            // handle success
            console.log(response);
          })
          .catch(function(error) {
            // handle error
            console.log(error);
          });
        break;
      case 32:
        console.log("Space");
        axios
          .get("http://localhost:3000/fireTorpedo")
          .then(function(response) {
            // handle success
            console.log(response);
          })
          .catch(function(error) {
            // handle error
            console.log(error);
          });
        break;
      default:
    }
  }
  componentDidMount() {
    document.addEventListener("keydown", this.escFunction, false);
  }
  componentWillUnmount() {
    document.removeEventListener("keydown", this.escFunction, false);
  }

  render() {
    return (
      <div className="App">
        <h1>Hello mini josh you scallywag.</h1>
        <h2>
          Tap WASD to move, Shift + Ctrl to go up and down, Space for torpedo,
          and ESC to brake.
        </h2>
        <input />
        <div width="100%">
          <iframe
            width="30%"
            height="480px"
            src="http://raspberrypi.local:8081"
          />
          <iframe
            width="30%"
            height="480px"
            src="http://raspberrypi.local:8082"
          />
          <iframe
            width="30%"
            height="480px"
            src="http://raspberrypi.local:8083"
          />
        </div>
      </div>
    );
  }
}

export default App;
