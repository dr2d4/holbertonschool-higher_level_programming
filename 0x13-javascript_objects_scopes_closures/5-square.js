#!/usr/bin/node
// Define class Rectangle

module.exports = class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }
};
