#!/usr/bin/mode

// Define the Square class that inherits from Rectangle
module.exports = class Square extends require('./4-rectangle') {
  constructor (size) {
    // Call the constructor of the Rectangle class with the size argument for both width and height
    super(size, size);
  }
}
