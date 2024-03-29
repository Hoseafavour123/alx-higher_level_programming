#!/usr/bin/node
// Display status code for a GET request

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
