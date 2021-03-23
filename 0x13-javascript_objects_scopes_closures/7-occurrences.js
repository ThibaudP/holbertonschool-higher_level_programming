#!/usr/bin/node
// Function that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  list.forEach(x => {
    if (x === searchElement) {
      i++;
    }
  });
  return i;
};
