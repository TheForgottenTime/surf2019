var five = require("johnny-five"); // Load the node library that lets us talk JS to the Arduino
var board = new five.Board(); // Connect to the Arduino using that library
var cors = require('cors');
var sleep = require('sleep')
var magnetometerData = {}
var accelerometerData = {}
var gyroscopeData = {}

var goingForward = false
var goingBackward = false
var goingLeft = false
var goingRight = false
var goingDown = false
var goingUp = false

var isGoingThroughGate = false



var intendedHeading = 0
board.on("ready", function () { // Once the computer is connected to the Arduino
    // Save convenient references to the LED pin and an analog pin
    // max forward 1900
    // max reverse 1100
    // stop 1500
    var express = require('express'); // Load the library we'll use to set up a basic webserver
    var app = express(); // And start up that server
    var expressWs = require('express-ws')(app);
    var escs = new five.ESCs([7, 9, 5, 4, 3, 2]);

    //setup the repl so we can control it via command line.
    board.repl.inject({
        escs: escs
    });
    /*
        var escs = new five.ESCs([{
                pin: 7,
                device: "FORWARD_REVERSE",
                pwmRange: [1100, 1900],
                neutral: 50,
            }, // Attached to an Adafruit PWM shield
            {
                pin: 9,
                device: "FORWARD_REVERSE",
                pwmRange: [1100, 1900],
                neutral: 50,
            }, // Attached directly to the Arduino
            {
                pin: 5,
                device: "FORWARD_REVERSE",
                pwmRange: [1100, 1900],
                neutral: 50,
            },
            {
                controller: "PCA9685",
                pin: 4,
                device: "FORWARD_REVERSE",
                pwmRange: [1100, 1900],
                neutral: 50,
            },
            {
                controller: "PCA9685",
                pin: 3,
                device: "FORWARD_REVERSE",
                pwmRange: [1100, 1900],
                neutral: 50,
            },
            {
                controller: "PCA9685",
                pin: 2,
                device: "FORWARD_REVERSE",
                pwmRange: [1100, 1900],
                neutral: 50,
            }
        ]);
    */
    escs.speed(50)

    app.use(cors())

    app.use(function (req, res, next) {

        next();
    });

    var imu = new five.IMU({
        controller: "BNO055",
        enableExternalCrystal: true
    });

    var torpedoServo = new five.Servo(44)
    this.repl.inject({
        servo: torpedoServo
    });
    //pressure sensor is 7
    app.get('/', function (req, res) { // what happens when we go to `/`
        res.send("I'm subby and im a garbage sub."); // Just send some text
    });

    app.get('/hello', function (req, res) { // what ha1ppens when we go to `/hello`
        res.sendFile('hello.html', {
            root: '.'
        }); // Send back the file `hello.html` located in the current directory (`root`)
    });

    app.get('/goForward', function (req, res) {
        if (goingForward) {
            escs[0].speed(50);
            escs[1].speed(50);
            goingForward = false;
            res.status(200).send("Done")
        } else {
            escs[0].speed(20);
            escs[1].speed(20);
            goingForward = true;
            res.status(200).send("Done")
        }
    });

    app.get('/goBackward', function (req, res) {
        if (goingBackward) {
            escs[0].speed(50);
            escs[1].speed(50);
            goingBackward = false;
            res.status(200).send("Done")
        } else {
            escs[0].speed(80);
            escs[1].speed(80);
            goingBackward = true;
            res.status(200).send("Done")
        }
    });

    app.get('/goUp', function (req, res) {
        if (goingUp) {
            escs[2].speed(50);
            escs[3].speed(50);
            escs[4].speed(50);
            escs[5].speed(50);
            goingUp = false
            res.status(200).send("Done")
        } else {
            escs[2].speed(80);
            escs[3].speed(80);
            escs[4].speed(80);
            escs[5].speed(80);
            goingUp = true
            res.status(200).send("Done")
        }
    });

    app.get('/goDown', function (req, res) {
        if (goingDown) {
            escs[2].speed(50);
            escs[3].speed(50);
            escs[4].speed(50);
            escs[5].speed(50);
            goingDown = false
            res.status(200).send("Done")
        } else {
            //escs[2].speed(10);
            //escs[3].speed(10);
            //escs[4].speed(80);
            //escs[5].speed(80);
            escs[2].speed(20);
            escs[3].speed(20);
            escs[4].speed(20);
            escs[5].speed(20);
            goingDown = true
            res.status(200).send("Done")
        }
    });

    app.get('/turnLeft', function (req, res) {
        // Set the motors to their max speed
        if (goingLeft) {
            escs[1].speed(50);
            escs[2].speed(50);
            goingLeft = false;
            res.status(200).send("Done")
        } else {
            escs[1].speed(60);
            escs[2].speed(40);
            goingLeft = true;
            res.status(200).send("Done")
        }
    });

    app.get('/turnRight', function (req, res) {
        if (goingRight) {
            escs[1].speed(50);
            escs[2].speed(50);
            goingRight = false;
            res.status(200).send("Done")
        } else {
            escs[1].speed(40);
            escs[2].speed(60);
            goingRight = true;
            res.status(200).send("Done")
        }
    });

    app.get('/brake', function (req, res) {
        // Set the motors to their max speed
        escs.brake();
        res.send("WHY WOULD YOU DO THIS TO ME, CAPTAIN!")
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

    app.get('/depth', function (req, res) {
        var analog = new five.Pin("A7");

        // Query the analog pin for its current state.
        analog.query(function (state) {
            console.log("Depth: " + state.value);
            res.status(200).send(state.value.toString())
        });
    })

    app.get('/holdDepth', function (req, res) {
        var speed = Number(req.query.speed)
        escs[2].speed(speed);
        escs[3].speed(speed);
        escs[4].speed(speed);
        escs[5].speed(speed);
        res.status(200).send("Done")
    })

    app.get('/releaseDepth', function (req, res) {
        escs[2].speed(50);
        escs[3].speed(50);
        escs[4].speed(50);
        escs[5].speed(50);
        res.status(200).send("Done")
    })

    app.ws('/ws', function (ws, req) {
        ws.send({
            accelerometerData,
            gyroscopeData,
            magnetometerData,
        })
    });

    app.get('/fireTorpedo', function (req, res) {
        torpedoServo.to(180);
        board.wait(2000, function () {
            torpedoServo.center();
            res.send("Fired away captain!")
        })
    });

    app.listen(3000, function () { // Actually turn the server on
        console.log("Server's up at http://localhost:3000!");
    });

    /* imu.on("calibrated", function () {
        console.log("I've been calibrated.")
        console.log("Now getting ready for the gate.")
        goThroughGate()
    }) */

    imu.on("data", function () {
        if (!isGoingThroughGate) {
            goThroughGate()
            isGoingThroughGate = true
        }
        /* console.log("Thermometer");
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
        console.log("--------------------------------------"); */
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
        /*  console.log("Gyroscope");
         console.log("  x            : ", this.gyro.x);
         console.log("  y            : ", this.gyro.y);
         console.log("  z            : ", this.gyro.z);
         console.log("  pitch        : ", this.gyro.pitch);
         console.log("  roll         : ", this.gyro.roll);
         console.log("  yaw          : ", this.gyro.yaw);
         console.log("  rate         : ", this.gyro.rate);
         console.log("  isCalibrated : ", this.gyro.isCalibrated);
         console.log("--------------------------------------"); */
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
        /*  console.log("magnetometer");
         console.log("  heading : ", Math.floor(this.magnetometer.heading)); */
        // console.log("  bearing : ", this.magnetometer.bearing.name);
        magnetometerData = {
            heading: Math.floor(this.magnetometer.heading),
        }

        //console.log("--------------------------------------");
    });

    function submerge() {
        console.log("Submerging.")
        escs[2].speed(20);
        escs[3].speed(20);
        escs[4].speed(20);
        escs[5].speed(20);
    }

    function emerge() {
        console.log("Emerging.")
        escs[2].speed(50);
        escs[3].speed(50);
        escs[4].speed(50);
        escs[5].speed(50);
    }

    async function goThroughGate() {

        console.log("You have 50 seconds to orient me towards the direction you want to keep.")
        setTimeout(() => {
            intendedHeading = magnetometerData.heading
            console.log("Heading locked, launching in 10 seconds")
        }, 50000)

        setTimeout(() => {
            console.log("Beginning gate run.")
            //Go down
            escs[2].speed(20);
            escs[3].speed(20);
            escs[4].speed(20);
            escs[5].speed(20);

            //Go forward
            escs[0].speed(20);
            escs[1].speed(20);
        }, 60000)

        setTimeout(() => {
            console.log("Concluding gate run.")
            escs[0].speed(50);
            escs[1].speed(50);

            escs[2].speed(50);
            escs[3].speed(50);
            escs[4].speed(50);
            escs[5].speed(50);
        }, 90000)
    }


    /*  function logEvery2Seconds(i) {
        setTimeout(() => {
            if (gyroscopeData.isCalibrated) {

                //handle pitch stablization
                if (gyroscopeData.pitch.angle < -10.00) {
                    escs[3].speed(60)
                    escs[4].speed(60)
                } else if (gyroscopeData.pitch.angle > 10.00) {
                    escs[3].speed(40)
                    escs[4].speed(40)
                } else {
                    escs[3].speed(50)
                    escs[4].speed(50)
                }

                //handle roll stablization
                if (gyroscopeData.roll.angle < -10.00) {
                    escs[2].speed(60)
                    escs[3].speed(60)

                } else if (gyroscopeData.roll.angle > 10.00) {
                    escs[2].speed(40)
                    escs[3].speed(40)
                } else {
                    escs[2].speed(50)
                    escs[3].speed(50)
                }
            }
            logEvery2Seconds(++i);
        }, 100)
    }
    logEvery2Seconds(0);
 */


})