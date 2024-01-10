#!/usr/bin/node
const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }

    for (let j = 0; j < this.height; j++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
