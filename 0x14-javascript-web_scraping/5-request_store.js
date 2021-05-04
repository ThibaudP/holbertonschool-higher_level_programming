#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  fs.writeFile(process.argv[3], body, err => {
    if (err) {
      console.error(err);
    }
  });
});
