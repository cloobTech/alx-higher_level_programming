#!/usr/bin/node

// Import the Rectangle class
const Rectangle = require('./5-square');

// Define the Square class that inherits from Rectangle
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let i = 0;
    while (i < this.width) {
      console.log(c.repeat(this.width));
      i++;
    }
  }
}

// Export the Square class
module.exports = Square;
