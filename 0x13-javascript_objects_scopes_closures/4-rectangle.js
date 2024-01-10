#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x = this.height;
    while (x) {
      console.log('X'.repeat(this.width));
      x--;
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    const change = this.width;
    this.width = this.height;
    this.height = change;
  }
};
