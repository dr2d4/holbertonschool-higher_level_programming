#!/usr/bin/node
// Manage file in nodejs

const request = require('request');
const url = process.argv[2];
const obj = {};

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const respt = JSON.parse(body);

  for (const i in respt) {
    if (respt[i].completed) {
      if (respt[i].userId in obj) {
        obj[respt[i].userId]++;
      } else {
        obj[respt[i].userId] = 1;
      }
    }
  }

  console.log(obj);
});
