#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const character = 'X';
    for (let j = 0; j < this.height; j++) {
      console.log(character.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
