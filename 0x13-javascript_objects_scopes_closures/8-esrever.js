#!/usr/bin/node

exports.esrever = function (list) {
  const reversedArray = [];

  list.forEach((item, index) => {
    reversedArray.unshift(list[index]);
  });
  return reversedArray;
};
