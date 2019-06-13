var array = ['a'];
var array_rssi = ['a'];
function except_duplex(data){
	var number_data = array.indexOf('"'+data.uuid+'"')
	console.log(number_data)
	if(number_data == -1){
		array.unshift('"'+data.uuid+'"');
		array_rssi.unshift('"'+data.rssi+'"');
	}
}

start_ms =new Date().getTime();
var count = 0
var Bleacon = require("bleacon");
Bleacon.startScanning();


Bleacon.on("discover", function(bleacon) {
    
    var elapsed_ms =new Date().getTime() -start_ms;
    console.log(elapsed_ms);
    if(elapsed_ms>=5000){
        Bleacon.stopScanning();
        process.exit(0);
    }
    
    payload = {"uuid" : bleacon['uuid'],
	           "rssi" : bleacon['rssi']}
	except_duplex(payload)
	console.log("test"+array+array_rssi)
    count = count+1
	var elapsed_ms =new Date().getTime() -start_ms;
    console.log(elapsed_ms)
	if (count>5){
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


