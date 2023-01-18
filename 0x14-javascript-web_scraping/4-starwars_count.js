#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
let count = 0;
request.get(url, function (error, response, body) {
  if (error) console.log(error);
  else {
    const films = JSON.parse(body).results;
    for (const film of films) {
      for (const character of film.characters) {
        if (character.search('18') > 0) count++;
      }
    }
    console.log(count);
  }
});
