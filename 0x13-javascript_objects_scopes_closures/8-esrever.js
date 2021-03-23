#!/usr/bin/node
// Function that reverses a list

exports.esrever = function (list) {
  const newList = [];
  list.forEach(x => {
    newList.unshift(x);
  });
  return newList;
};
