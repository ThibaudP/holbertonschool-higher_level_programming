#!/usr/bin/node
// Finds the second biggest number in an array

let second = 0;
const array = process.argv.slice(2);
const len = array.length;

if (len > 1) {
  array.sort();
  second = array[array.length - 2];
}
console.log(second);
