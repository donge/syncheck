var express = require('express');
var bodyParser = require('body-parser');
var app = express();

var commits = [ {svn:10000}, {svn:20000}, {svn:30000}];
var pr12345 = [ {svn:11111}, {svn:22222}, {svn:33333}];
app.use('/', express.static(__dirname));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

app.get('/commits.json', function(req, res) {
  res.setHeader('Content-Type', 'application/json');
  res.send(JSON.stringify(commits));
});

app.post('/commits.json', function(req, res) {
  commits.push(req.body);
  res.setHeader('Content-Type', 'application/json');
  res.send(JSON.stringify(commits));
});


app.get('/pr/12345', function(req, res) {
  res.setHeader('Content-Type', 'application/json');
  res.send(JSON.stringify(pr12345));
});

app.listen(3000);

console.log('Server started: http://localhost:3000/');