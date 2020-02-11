#!/usr/bin/node
// Define class Rectangle

exports.converter = function (base) {
  return function mainConvert (num) {
    return num.toString(base);
  };
};
