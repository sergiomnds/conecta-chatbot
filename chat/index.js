var app = require('express')();
var http = require('http');
var server = http.Server(app)
var io = require('socket.io')(server);
var port = process.env.PORT || 3000;
const urlRobo = "http://127.0.0.1:5000/resposta/";

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});

getRespostaRobo = (msg) => {
  let data = "";

  http.get(urlRobo + msg, (resposta) => {
    resposta.on("data", (chunk) => {
      data += chunk;
    });

    resposta.on("end", () => {
      io.emit('chat message', "Conecta: " + data);
    });

  })
}

io.on('connection', function (socket) {
  socket.on('chat message', function (msg) {
    io.emit('chat message', "Cliente: " + msg);
    getRespostaRobo(msg);
  });
});

server.listen(port, function () {
  console.log('Server na porta:' + port);
});
