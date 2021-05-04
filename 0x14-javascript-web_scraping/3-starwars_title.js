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
  console.log(body.title);
});
