#!/usr/bin/node
// Print the number of tasks completed by id

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(body);
    const users = {};

    for (let i = 0; i < todos.length; i++) {
      if (todos[i].completed) {
        if (users[todos[i].userId]) {
          users[todos[i].userId] += 1;
        } else {
          users[todos[i].userId] = 1;
        }
      }
    }
    console.log(users);
  }
});
