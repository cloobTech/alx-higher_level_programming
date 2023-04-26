#!/usr/bin/node

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
const request = require('request');

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    if (res.statusCode === 200) {
      const data = JSON.parse(body);

      const characters = data.characters;
      characters.forEach(character => {
        request(character, (err, res, body) => {
          if (!err) {
            console.log(JSON.parse(body).name);
          }
        });
      });
    }
  }
});
