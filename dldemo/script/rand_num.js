function periodic() {
    var d = document.getElementById('egdiv');
    d.innerHTML = 'Random number: ' + Math.random();
}
 
var net; // declared outside -> global variable in window scope
function start() {
    // this gets executed on startup
    //... 
    net = new convnetjs.Net();
    // ...
    
    // example of running something every 1 second
    setInterval(periodic, 1000);
}
