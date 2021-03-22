#!/usr/bin/node
// Prints the first argument passed to the script

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
