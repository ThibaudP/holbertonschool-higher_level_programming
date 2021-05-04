#!/usr/bin/node
const request = require('request');
const api = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];
const url = api + id;

request(url, { json: true }, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const cast = body.characters;

  for (const characterUrl of cast) {
    request(characterUrl, { json: true }, (err, response, body) => {
      if (err) {
        console.error(err);
      } else {
        console.log(body.name);
      }
    });
  }
});
