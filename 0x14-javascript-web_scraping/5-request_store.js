#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filePath, body, 'utf8', (error) => {
      if (error) {
        console.error(error);
      } else {
        console.log(`Successfully saved response body to ${filePath}`);
      }
    });
  }
});
