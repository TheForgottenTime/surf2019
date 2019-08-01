# Mizzou SURF

This is the code for the Mizzou SURF robot.

## Connect to Raspberry Pis

Use a utility like Angry IP Scanner to scan your ethernet network for IPs. Disconnect from wifi if needed.

If you still can't find the ip, try:

```
ssh pi@raspberrypi.local
ssh pi@raspberrypi-2.local
```

and then do

```
ifconfig
```

and note the ip address. That's the IP that the PI is on your network.

## Installation

Fetch the repo into the raspberry pi and your machine.

On the Pi:

```bash
./startCamera.sh
cd NodeJS
npm install
node motorControl.js
```

The sub should now be powered on.

On your laptop (starting the web site):

```bash
cd webcontroller
npm install
npm start
```

Navigate to localhost:3000 to view the page.

Change

```bash
 <iframe width="640px" height="480px" src="http://192.168.2.XX:XXXX" />
```

to

```bash
 <iframe width="640px" height="480px" src="http://192.168.2.XX:XXXX" />
```

if the image isn't showing up. Also check the WASD controls in console. Change the IP in app.js if needed.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
