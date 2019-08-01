import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";
import Button from "@material-ui/core/Button";
import Websocket from "react-websocket";
const axios = require("axios");
class App extends Component {
  constructor(props) {
    super(props);
    this.escFunction = this.escFunction.bind(this);
    this.state = {
      count: 90
    };
  }

  handleData(data) {
    let result = JSON.parse(data);
    console.log(result);
    this.setState({
      count: this.state.count + result.movement
    });
  }

  escFunction(event) {
    if (event.repeat) {
      return;
    } else {
      switch (event.keyCode) {
        case 27:
          console.log("Escape");
          axios
            .get("http://192.168.2.18:3000/brake")
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
            .get("http://192.168.2.18:3000/goForward")
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
            .get("http://192.168.2.18:3000/turnLeft")
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
            .get("http://192.168.2.18:3000/goBackward")
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
            .get("http://192.168.2.18:3000/turnRight")
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
            .get("http://192.168.2.18:3000/goUp")
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
            .get("http://192.168.2.18:3000/goDown")
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
            .get("http://192.168.2.17:3000/fireTorpedo")
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
  }

  escRelease(event) {
    console.log("Released");
  }

  componentDidMount() {
    document.addEventListener("keydown", this.escFunction, false);
    document.addEventListener("keyup", this.escFunction, false);
  }
  componentWillUnmount() {
    document.removeEventListener("keydown", this.escFunction, false);
  }

  render() {
    return (
      <div className="App">
        <h1> Hello mini josh you scallywag. </h1>{" "}
        <h2>
          Tap WASD to move, Shift + Ctrl to go up and down, Space for torpedo,
          and ESC to brake.{" "}
        </h2>{" "}
        <input />
        <div width="100%">
          <iframe width="640px" height="480px" src="http://192.168.2.17:8081" />
          <iframe width="640px" height="480px" src="http://192.168.2.17:8082" />
        </div>
        <iframe width="1280px" height="720px" src="http://192.168.2.18:8081" />
        <div>
          <Websocket
            url="ws://192.168.1.18:3000/ws"
            onMessage={this.handleData.bind(this)}
          />{" "}
          <h3> Gyroscope </h3>{" "}
        </div>{" "}
      </div>
    );
  }
}

export default App;
