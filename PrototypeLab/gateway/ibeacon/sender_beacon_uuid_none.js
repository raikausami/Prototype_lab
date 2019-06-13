//https://gist.github.com/Xaekai/e1f711cb0ad865deafc11185641c632a
const SOCKETFILE = '../socket_file'
var array = ['a'];
var net = require( 'net' );
count_e = 0
var io = setInterval(function(){
        //console.log("finish")
        
        client = net.createConnection(SOCKETFILE)
		.on('connect',()=>{
            client.write('[]'+'\n')
            client.flush
            count_e = count_e+1
            //if(count_e==3) client.close
		})
		.on('data',function(data){
			data = data.toString();
			client.write('2')
		})
		.on('error',function(data){
			process.exit(1)
		});
        /*
        client.write('[]'+'\n')
        client.flush
        count_e = count_e+1
        if(count_e==3) client.close
        */
        },2000);
start_ms =new Date().getTime();
var Bleacon = require("bleacon");
beacon_discover()


var counti = 0 
function client_communicate(str_2){
	client = net.createConnection(SOCKETFILE)
		.on('connect',()=>{
			//if (counti = 2){
			//	process.exit(1)
			//}
			//console.log("Connected.\n");
			counti = counti + 1
			if(counti==1){

				client.write(str_2+'\n')
				client.flush
				start_ms =new Date().getTime();
                //client.write('1')
			}
			//console.log(str_2)
			////////////////client.write(str_2);
			//client.write(str_2);
			//
			
			
				
		})   
		.on('data',function(data){
			data = data.toString();
			client.write('2')
		})
		.on('error',function(data){
			process.exit(1)
		});
}


function except_duplex(data){
	var number_data = array.indexOf('"'+data+'"')
	//console.log(number_data)
	if(number_data == -1){
		array.unshift('"'+data+'"');
	}
}

function beacon_discover(){

    var count = 0

    Bleacon.startScanning();
    Bleacon.on("discover", function(bleacon) {
        payload = {"uuid" : bleacon['uuid'],
                   "rssi" : bleacon['rssi']}
        except_duplex(payload.uuid)
        count = count+1
        //var elapsed_ms =new Date().getTime() -start_ms;
        if (count>5){
            //console.log(elapsed_ms);
            array.unshift('[')
            array.pop();
            array.push(']')
            str = array.join(',');
            var str_2 = str.slice(0,1)+str.slice(2,-2)+str.slice(-1)
            //console.log(str_2);
          //process.exit(0);
            client_communicate(str_2);
	    //process.exit(0)

		
        }
        //console.log(payload);
    });
}


