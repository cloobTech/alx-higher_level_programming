#!/usr/bin/mode

// Import the Rectangle class
const Rectangle = require('./4-rectangle');

// Define the Square class that inherits from Rectangle
module.exports = class Square extends Rectangle {
  constructor (size) {
    // Call the constructor of the Rectangle class with the size argument for both width and height
    super(size, size);
  }
}
