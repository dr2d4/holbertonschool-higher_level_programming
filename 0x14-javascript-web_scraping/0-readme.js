#!/usr/bin/node
// Manage file in nodejs

const file = process.argv[2];
const fs = require('fs');

fs.readFile(file, 'utf8', (err, contents) => {
  if (!err) {
    console.log(contents);
  } else {
    console.log(err);
  }
});
