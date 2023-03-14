#!/usr/bin/node

const data = require('./100-data.js').list;

const newData = data.map((item, index) => item * index);

console.log(data);
console.log(newData);
