#!/usr/bin/node
// the square class inherits from the rectangle
const nSquare = require('./5-square');

class Square extends nSquare {
  charPrint (c) {
    for (let count = 0; count < this.height; count++) {
      if (c === undefined) {
        console.log('X'.repeat(this.width));
      } else {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
