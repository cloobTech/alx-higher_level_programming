#!/usr/bin/node

// Import the Rectangle class
const Rectangle = require('./4-rectangle');

// Define the Square class that inherits from Rectangle
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c = 'X') {
    let i = 0;
    while (i < this.size) {
      console.log(c.repeat(this.size));
      i++;
    }
  }
}

// Export the Square class
module.exports = Square;
