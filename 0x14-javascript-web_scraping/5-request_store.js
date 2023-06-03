#!/usr/bin/node
// Request for a webpage and store to a file

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];

request(url, 'utf8').pipe(fs.createWriteStream(file));
