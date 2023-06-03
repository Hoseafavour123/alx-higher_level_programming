#!/usr/bin/node
// Writes a string to a file

const fs = require('fs');
const file = process.argv[2];
const str = process.argv[3];

fs.writeFile(file, str, 'utf8', function (error) {
  if (error) {
    console.log(error);
  }
});
