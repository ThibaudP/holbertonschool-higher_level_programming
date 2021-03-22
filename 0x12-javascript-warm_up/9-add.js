#!/usr/bin/node
// Adds the first two arguments (which must be integers), in a function

function add (a, b) {
  return a + b;
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

const res = add(a, b);
console.log(res);
