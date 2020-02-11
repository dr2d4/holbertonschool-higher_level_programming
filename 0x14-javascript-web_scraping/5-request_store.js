#!/usr/bin/node
// Manage file in nodejs

const request = require('request');
const file = process.argv[3];
const url = process.argv[2];
const fs = require('fs');

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  fs.writeFile(file, body, (err) => {
    if (err) console.log(err);
  });
});
