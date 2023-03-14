#!/usr/bin/mode

// Import the Rectangle class
const Rectangle = require('./4-rectangle');

// Define the Square class that inherits from Rectangle
class Square extends Rectangle {
  constructor (size) {
    // Call the constructor of the Rectangle class with the size argument for both width and height
    super(size, size);
  }
}

// Export the Square class
module.exports = Square;
