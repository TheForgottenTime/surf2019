var five = require("johnny-five");
var board = new five.Board();

board.on("ready", function () {

    var compass = new five.IMU({
        controller: "BNO055",
        enableExternalCrystal: false
    });

    compass.on("change", function () {
        console.log("change");
    });

    compass.on("calibrated", function () {
        console.log("calibrated");
    });

    compass.on("data", function () {
        console.log("Data")
    });
});