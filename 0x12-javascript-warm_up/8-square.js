#!/usr/bin/node
// Prints a square. Size of square is first argument

const c = 'X';
const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    console.log(c.repeat(num));
  }
}
