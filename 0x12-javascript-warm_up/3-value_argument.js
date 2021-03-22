#!/usr/bin/node
// Prints the first argument passed to the script

if (!process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
