#!/usr/bin/node
// Function that converts a number from base10 to another base passed as argument

exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
