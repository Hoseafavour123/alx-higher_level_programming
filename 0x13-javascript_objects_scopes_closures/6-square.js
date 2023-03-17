#!/usr/bin/node

const SquareB = require('./5-square');

module.exports = class Square extends SquareB {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let l = '';

    for (let i = 1; i <= this.width; i++) {
      l += c;
    }
    for (let j = 1; j <= this.height; j++) {
      console.log(l);
    }
  }
};
