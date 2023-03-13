#!/usr/bin/node

let count = 0;
const times = parseInt(process.argv[2]);
const str = ['C is fun'];

if (isNaN(times)) {
  console.log('Missing number of occurrences');
} else {
  while (count < times) {
    str.forEach((alpha) => console.log(alpha));
    count++;
  }
}
