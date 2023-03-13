#!/usr/bin/node

import { argv } from 'node:process';
let result = '';

// print process.argv
if (argv.length === 2) {
  result = 'No argument';
} else if (argv.length === 3) {
  result = 'Argument found';
} else if (argv.length >= 4) {
  result = 'Arguments found';
}

console.log(result);
