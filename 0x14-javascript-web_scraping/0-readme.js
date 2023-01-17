#!/usr/bin/node
// A script that reads and prints the content of a file
const myfile = process.argv[2];
const fs = require('fs');
// Reading the file
fs.readFile(myfile, 'utf8', function (err, data) {
  if (err) {
    return console.error(err);
  } else {
    return console.log(data.toString());
  }
});
