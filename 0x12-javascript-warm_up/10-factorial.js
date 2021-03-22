#!/usr/bin/node
// Computes the factorial of a number

function factorial (a) {
  if (isNaN(a) || a <= 1) {
    return 1;
  } else {
    return (a * factorial(a - 1));
  }
}

const a = parseInt(process.argv[2]);

const res = factorial(a);
console.log(res);
