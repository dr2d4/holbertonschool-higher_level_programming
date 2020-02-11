#!/usr/bin/node
// Define class Rectangle

exports.esrever = function (list) {
  let res = [];

  for (let i = list.length - 1; i >= 0; i--) {
    res.push(list[i]);
  }

  return res;
};
