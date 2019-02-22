var array = ['a'];
function except_duplex(data){
	var number_data = array.indexOf('"'+data+'"')
	console.log(number_data)
	if(number_data == -1){
		array.unshift('"'+data+'"');
	}
}

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
		console.log(str_2);
		process.exit(0);
	}
	console.log(payload);
});


