#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const cast = 'https://swapi-api.alx-tools.com/api/people/18/';

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  }
  if (res.statusCode === 200) {
    const data = JSON.parse(body);
    let count = 0;
    const results = data.results;

    results.forEach((episode) => {
      const characters = episode.characters;

      if (characters.includes(cast)) {
        count++;
      }
    });

    console.log(count);
  }
});
