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
      const outputArray = [];
      const regex = /\<\d+ empty item(s)?\>/;
      characters.forEach((character, index) => {
        request(character, (err, res, body) => {
          if (!err) {
            const castName = JSON.parse(body).name;
            outputArray[index] = castName;
            if ((outputArray.length === characters.length) && outputArray.every(str => !regex.test(str))) {
              outputArray.forEach(str => console.log(str));
            }
          }
        });
      });
    }
  }
});
