#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};
let key;

for (key in dict) {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [];
  }
  newDict[dict[key]].push(key);
}

console.log(newDict);