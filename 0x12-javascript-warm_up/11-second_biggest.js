#!/usr/bin/node
// Finds the second biggest number in an array

if (process.argv.length < 4) {
  console.log('0');
} else {
  const array = process.argv.slice(2);
  array.map(x => parseInt(x));
  array.sort();
  console.log(array[array.length - 2]);
}
