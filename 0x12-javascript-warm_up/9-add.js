#!/usr/bin/node

const firstValue = parseInt(process.argv[2]);
const secondValue = parseInt(process.argv[3]);

if (typeof process.argv[2] === 'undefined') {
    console.log('NaN');
} else if (isNaN(firstValue || secondValue)) {
  console.log('NaN');
} else {
    console.log(firstValue + secondValue);
}
