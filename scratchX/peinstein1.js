(function(ext) {
    var device = null;
    var in_data = "";
    var valid_dongle = false;
    // Extension API interactions
    var potentialDevices = [];
    ext._deviceConnected = function(dev) {
        potentialDevices.push(dev);

        if (!device) {
            tryNextDevice();
        }
    }

    function tryNextDevice() {
        // If potentialDevices is empty, device will be undefined.
        // That will get us back here next time a device is connected.
        device = potentialDevices.shift();
        if (!device) return;

        device.open({ stopBits: 0, bitRate: 115200, ctsFlowControl: 0 });
        device.set_receive_handler(function(data) {
            console.log('Received: ' + data.byteLength);
            //if(!rawData) rawData = new Uint8Array(data);
            //else rawData = appendBuffer(rawData, data);
                //console.log(rawData);
                //processData();
                //device.send(pingCmd.buffer);
                console.log('data' + data);
                in_data = in_data.concat(data);
                console.log('in data' + in_data);
        });
        //set init.lua to load peinstein1.lua
        device.send('print_dongle()\n');//should return peinstein
    };

    ext._deviceRemoved = function(dev) {
        if(device != dev) return;
        device = null;
    };

    ext._shutdown = function() {
        if(device) device.close();
        device = null;
    };

    ext._getStatus = function() {
        if(!device) return {status: 1, msg: 'P.E. Dongle disconnected'};
        //if(watchdog) return {status: 1, msg: 'Probing for P.E. Dongle'};
        return {status: 2, msg: 'P.E. Dongle connected'};
    };

    var function_state=0;

    ext.connect = function() {
      if (!device) return;
      function_state = 1;
      device.send("connect_tcp()\n");
    };
/*
    ext.is_ready = function() {
      if (!device) return false;
      function_state = 2;
      device.send("is_ready()\n");
    };
    */
    ext.say = function(says,callback) {
      if (!device) return;
      device.send(says);
      window.setTimeout(function(){
        callback();
      },1000);
    };
/*
    var descriptor = {
        blocks: [
            ['h', 'when %m.booleanSensor',         'whenSensorConnected', 'button pressed'],
            ['h', 'when %m.sensor %m.lessMore %n', 'whenSensorPass',      'slider', '>', 50],
            ['b', 'sensor %m.booleanSensor?',      'sensorPressed',       'button pressed'],
            ['r', '%m.sensor sensor value',        'sensor',              'slider']
        ],
        menus: {
            booleanSensor: ['button pressed', 'A connected', 'B connected', 'C connected', 'D connected'],
            sensor: ['slider', 'light', 'sound', 'resistance-A', 'resistance-B', 'resistance-C', 'resistance-D'],
            lessMore: ['>', '<']
        },
    };
    */
    var descriptor = {
        blocks: [
          [' ', 'connect', 'connect'],
          //[' ', 'is robot ready', 'is_ready'],
          ['R', 'say %s', 'say','hello']
        ]
      };

    ScratchExtensions.register('peDongle', descriptor, ext, {type: 'serial'});
})({});
