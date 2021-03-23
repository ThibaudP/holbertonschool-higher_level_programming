#!/usr/bin/node
// Function that increments a counter everytime it's called
let count = 0;

exports.logMe = function (elem) {
  console.log(count + ': ' + elem);
  count++;
};
