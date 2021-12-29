// Load environment variables from .env
require('dotenv').config();

// Import HTTP package
const http = require('http');

http.createServer(function (request, response) {
   target = process.env.TARGET ? process.env.TARGET : 'World';
   
   msg = process.env.MSG ? process.env.MSG : 'Hello ' + target + '!\n';
   
   response.writeHead(200, {'Content-Type': 'text/plain'});
   response.end(msg);
}).listen(process.env.PORT);

console.log('Server running on PORT:', process.env.PORT);
