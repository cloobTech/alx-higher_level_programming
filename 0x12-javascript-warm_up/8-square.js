#!/usr/bin/node

let count = 0;
const times = parseInt(process.argv[2]);
const star = 'X';

if (isNaN(times)) {
  console.log('Missing size');
} else {
  while (count < times) {
    console.log(star.repeat(times));
    count++;
  }
}
