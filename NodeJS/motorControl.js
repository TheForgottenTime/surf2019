var five = require("johnny-five"); // Load the node library that lets us talk JS to the Arduino
var board = new five.Board(); // Connect to the Arduino using that library

var magnetometerData = {}
var accelerometerData = {}
var gyroscopeData = {}
board.on("ready", function () { // Once the computer is connected to the Arduino
    // Save convenient references to the LED pin and an analog pin
    // max forward 1900
    // max reverse 1100
    // stop 1500
    var express = require('express'); // Load the library we'll use to set up a basic webserver
    var app = express(); // And start up that server
    var escs = new five.ESCs([7, 9, 5, 4, 3, 2]);
    escs.speed(50)
    var imu = new five.IMU({
        controller: "BNO055"
    });

    app.get('/', function (req, res) { // what happens when we go to `/`
        res.send("I'm subby and im a garbage sub."); // Just send some text
    });

    app.get('/hello', function (req, res) { // what ha1ppens when we go to `/hello`
        res.sendFile('hello.html', {
            root: '.'
        }); // Send back the file `hello.html` located in the current directory (`root`)
    });

    app.get('/goForward', function (req, res) {
        // Set the motors to their max speed
        escs[0].speed(60);
        escs[1].speed(60);
        board.wait(2000, function () {
            // Set the motors to the min speed (stopped)
            escs[0].speed(50);
            escs[1].speed(50);
            res.send("Done")
        });
    });

    app.get('/accelerometer', function (req, res) { // what happens when someone goes to `/led/off`
        res.status(200).json(accelerometerData)
    });

    app.get('/gyroscope', function (req, res) { // what happens when someone goes to `/led/off`
        res.status(200).json(gyroscopeData)
    });

    app.get('/magnetometer', function (req, res) {
        res.status(200).json(magnetometerData)
    });

    app.listen(3000, function () { // Actually turn the server on
        console.log("Server's up at http://localhost:3000!");
    });

    imu.on("change", function () {
        console.log("Thermometer");
        console.log("  celsius      : ", this.thermometer.celsius);
        console.log("  fahrenheit   : ", this.thermometer.fahrenheit);
        console.log("  kelvin       : ", this.thermometer.kelvin);
        console.log("--------------------------------------");

        console.log("Accelerometer");
        console.log("  x            : ", this.accelerometer.x);
        console.log("  y            : ", this.accelerometer.y);
        console.log("  z            : ", this.accelerometer.z);
        console.log("  pitch        : ", this.accelerometer.pitch);
        console.log("  roll         : ", this.accelerometer.roll);
        console.log("  acceleration : ", this.accelerometer.acceleration);
        console.log("  inclination  : ", this.accelerometer.inclination);
        console.log("  orientation  : ", this.accelerometer.orientation);
        console.log("--------------------------------------");
        accelerometerData = {
            x: this.accelerometer.x,
            y: this.accelerometer.y,
            z: this.accelerometer.z,
            pitch: this.accelerometer.pitch,
            roll: this.accelerometer.roll,
            acceleration: this.accelerometer.acceleration,
            inclination: this.accelerometer.inclination,
            orientation: this.accelerometer.orientation
        }
        console.log("Gyroscope");
        console.log("  x            : ", this.gyro.x);
        console.log("  y            : ", this.gyro.y);
        console.log("  z            : ", this.gyro.z);
        console.log("  pitch        : ", this.gyro.pitch);
        console.log("  roll         : ", this.gyro.roll);
        console.log("  yaw          : ", this.gyro.yaw);
        console.log("  rate         : ", this.gyro.rate);
        console.log("  isCalibrated : ", this.gyro.isCalibrated);
        console.log("--------------------------------------");
        gyroscopeData = {
            x: this.gyro.x,
            y: this.gyro.y,
            z: this.gyro.z,
            pitch: this.gyro.pitch,
            roll: this.gyro.roll,
            yaw: this.gyro.yaw,
            rate: this.gyro.rate,
            isCalibrated: this.gyro.isCalibrated
        }
        console.log("magnetometer");
        console.log("  heading : ", Math.floor(this.magnetometer.heading));
        // console.log("  bearing : ", this.magnetometer.bearing.name);
        magnetometerData = {
            heading: Math.floor(this.magnetometer.heading),
        }
        console.log("--------------------------------------");
    });
});