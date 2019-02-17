//https://gist.github.com/Xaekai/e1f711cb0ad865deafc11185641c632a
const SOCKETFILE = 'socket_file'
var array = ['a'];
var net = require( 'net' );

client = net.createConnection(SOCKETFILE)
    .on('connect',()=>{
        console.log("Connected.");
        client.write('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa');
    })

    .on('data', function(data) {
    
        data = data.toString();

        if(data === '__boop'){
            console.info('Server sent boop. Confirming our snoot is booped.');
            beacon_data = beacon_discover()
            client.write(beacon_data);
        }
        if(data === '__disconnect'){
            console.log('Server disconnected.')
            return cleanup();
        }

        // Generic message handler
        console.info('Server:', data)
    })

    .on('error', function(data) {
        console.error('Server not active.'); process.exit(1);
    });



function except_duplex(data){
	var number_data = array.indexOf('"'+data+'"')
	console.log(number_data)
	if(number_data == -1){
		array.unshift('"'+data+'"');
	}
}

function beacon_discover{
    var start_ms =new Date().getTime();
    var count = 0
    var Bleacon = require("bleacon");
    Bleacon.startScanning();
    Bleacon.on("discover", function(bleacon) {
        payload = {"uuid" : bleacon['uuid'],
                   "rssi" : bleacon['rssi']}
        except_duplex(payload.uuid)
        count = count+1
        var elapsed_ms =new Date().getTime() -start_ms;
        if (count>30){
            console.log(elapsed_ms);
            array.unshift('[')
            array.pop();
            array.push(']')
            str = array.join(',');
            var str_2 = str.slice(0,1)+str.slice(2,-2)+str.slice(-1)
            //console.log(str_2);
            //process.exit(0);
            return str2
        }
        console.log(payload);
    });
}


