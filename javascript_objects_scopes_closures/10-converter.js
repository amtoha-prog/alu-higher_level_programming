#!/usr/bin/node
// No imports and no new variables allowed, so the function is returned directly.
exports.converter = function (base) {
  return function (n) {
    return n.toString(base);
  };
};
