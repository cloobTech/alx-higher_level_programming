#!/usr/bin/node

let n = (parseInt(process.argv[2]));

if (isNaN(n)) n = 1;

const recur = (n) => {
  if (n === 1) {
    return 1;
  } else {
    return n * recur(n - 1);
  }
};

const result = recur(n);
console.log(result);
