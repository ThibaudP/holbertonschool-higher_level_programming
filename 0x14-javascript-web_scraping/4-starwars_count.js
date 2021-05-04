#!/usr/bin/node
const request = require('request');
const api = process.argv[2];
const id = 18;
const url = api;
let counter = 0;

request(url, { json: true }, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const films = body.results;
  for (const film of films) {
    for (const character of film.characters) {
      if (character.includes(id)) {
        counter++;
      }
    }
  }

  console.log(counter);
});
