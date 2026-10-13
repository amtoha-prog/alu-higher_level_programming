#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    // One row of X per unit of height. An empty rectangle prints nothing.
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;