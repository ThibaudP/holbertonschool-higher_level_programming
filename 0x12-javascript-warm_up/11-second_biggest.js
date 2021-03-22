#!/usr/bin/node
// Finds the second biggest number in an array

if (process.argv.length < 4) {
  console.log('0');
} else {
  let array = process.argv.slice(2);
  array = array.map(x => Number(x));
  array.sort();
  console.log(array[array.length - 2]);
}
