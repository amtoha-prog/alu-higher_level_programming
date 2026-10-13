#!/usr/bin/node
exports.esrever = function (list) {
  const reversed = [];
  // Walk the list from the last item to the first.
  for (let i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }
  return reversed;
};