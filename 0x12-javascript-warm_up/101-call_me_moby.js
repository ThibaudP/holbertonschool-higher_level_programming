#!/usr/bin/node
// Calls a function x times

exports.callMeMoby = function (x, func) {
  for (let i = 0; i < x; i++) {
    func();
  }
};
