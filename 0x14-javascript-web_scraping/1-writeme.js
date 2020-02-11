#!/usr/bin/node
// Manage file in nodejs

const content = process.argv[3];
const file = process.argv[2];
const fs = require('fs');

fs.writeFile(file, content, (err) => {
  if (err) console.log(err);
});
