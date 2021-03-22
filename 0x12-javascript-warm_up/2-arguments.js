#!/usr/bin/node
// Prints a message depending on arguments passed to script

if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else if (process.argv.length === 4) {
  console.log('Arguments found');
}
