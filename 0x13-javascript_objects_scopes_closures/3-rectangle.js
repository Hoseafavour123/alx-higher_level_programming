#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let l = '';

    for (let i = 1; i <= this.width; i++) {
      l += 'X';
    }
    for (let j = 1; j <= this.height; j++) {
      console.log(l);
    }
  }
};
