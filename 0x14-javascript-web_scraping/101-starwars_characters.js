#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, { json: true }, async (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const cast = body.characters;

    for (const characterUrl of cast) {
      const name = await new Promise((resolve, reject) => {
        request(characterUrl, { json: true }, (err, response, body) => {
          if (err) {
            reject(err);
          } else {
            resolve(body.name);
          }
        });
      });
      console.log(name);
    }
  }
});
