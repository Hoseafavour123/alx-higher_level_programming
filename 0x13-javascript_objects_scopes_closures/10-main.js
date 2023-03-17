#!/usr/bin/node

const converter = require('./10-converter').converter;

const myConverter = converter(16);
console.log(myConverter(12));
