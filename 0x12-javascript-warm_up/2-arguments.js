#!/usr/bin/node

let argv = process.argv

// print process.argv
if (argv.length === 2) {
  console.log('No argument');
} else if (argv.length === 3) {
  console.log('Argument found');
} else if (argv.length >= 4) {
  console.log('Arguments found');
}
