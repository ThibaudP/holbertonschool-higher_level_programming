#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, { json: true }, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const users = {};

  body.forEach(task => {
    if (task.completed) {
      if (task.userId in users) {
        users[task.userId] += 1;
      } else {
        users[task.userId] = 1;
      }
    }
  });
  console.log(users);
});
