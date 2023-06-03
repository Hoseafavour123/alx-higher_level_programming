#!/usr/bin/node
// Prints the title of movie from star wars API

const request = require('request');
const id = process.argv[2];

request('https://swapi-api.alx-tools.com/api/films/' + id, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const movie = JSON.parse(body);
    const title = movie.title;
    console.log(title);
  }
});
