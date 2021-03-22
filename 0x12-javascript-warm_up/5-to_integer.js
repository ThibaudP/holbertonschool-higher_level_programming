#!/usr/bin/node
// Parses a literal number to integer if possible and prind the result

const number = parseInt(process.argv[2]);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
