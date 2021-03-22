#!/usr/bin/node
// Prints * times (= first argument) a string

const string = 'C is fun';
const num = parseInt(process.argv[2]);

if (!num) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < num; i++) {
    console.log(string);
  }
}
