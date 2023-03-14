#!/usr/bin/node

const args = process.argv.slice(2);
const nums = args.map(Number);

if (nums.length < 2) {
  console.log(0);
} else {
  const largest = Math.max(...nums);
  const withoutLargest = nums.filter(num => num !== largest);
  const secondLargest = Math.max(...withoutLargest);
  console.log(secondLargest);
}
