#!/usr/bin/node

argv = process.argv;
let result = '';

// print process.argv
argv.forEach((val, index) => {
  if (index === 1) {
    result = 'No argument';
  } else {
    result = 'Argument found';
  }
});

console.log(result);
