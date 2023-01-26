#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
const movie_url = `https://swapi-api.alx-tools.com/api/films/${id}`;
let episode_title = null;
let count = 0;
request.get(movie_url, (error, response, body) => {
  if (error) throw error;
  else {
    const episode = JSON.parse(body);
    episode_title = episode.title;
  }
  request.get(url, (error, response, body) => {
    if (error) console.log(error);
    else {
      const result = JSON.parse(body);
      console.log(`Title: ${episode_title}`);
      for (const film of result.results) {
        if (film.title == episode_title) {
          console.log(film.characters);
          for (const character of film.characters) {
            console.log(character);
            count++;
            request(character, (error, response, body) => {
              if (error) console.log(error);
              else {
                console.log(JSON.parse(body));
              }
            });
            console.log(count);
          }
        }
      }
    }
  });
});
