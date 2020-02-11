#!/usr/bin/node
// Manage file in nodejs

const check = 'https://swapi.co/api/people/18/';
const request = require('request');
const url = process.argv[2];
let count = 0;

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const resp = JSON.parse(body);

  for (const i in resp.results) {
    if (resp.results[i].characters.includes(check)) {
      count++;
    }
  }

  console.log(count);
});
