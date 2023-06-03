#!/usr/bin/node
// A script that reads the content of a file and prints the data

const filePath = process.argv[2];
const fs = require('fs');

fs.readFile(filePath, 'utf8', function (error, data) {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
