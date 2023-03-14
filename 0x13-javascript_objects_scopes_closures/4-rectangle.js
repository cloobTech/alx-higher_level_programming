#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    while (i < this.height) {
      console.log('X'.repeat(this.width));
      i++;
    }
  }

  rotate () {
   let tmp = 0;
   tmp = this.width;
   this.width = this.height;
   this.height = tmp;
  }

  double () {
  this.width = this.width * 2;
  this.height = this.height * 2;
  }
};
