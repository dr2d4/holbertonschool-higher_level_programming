#!/usr/bin/node
exports.add = function callMeMoby(n, f) {
  for (let i = 0; i < n; i++)
  {
    f();
  }
}
