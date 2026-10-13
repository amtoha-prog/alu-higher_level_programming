#!/usr/bin/node
// Lives outside the function so it keeps its value between calls.
let printed = 0;

exports.logMe = function (item) {
  console.log(printed + ': ' + item);
  printed++;
};