#!/usr/bin/node

import { argv } from 'node:process';
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
