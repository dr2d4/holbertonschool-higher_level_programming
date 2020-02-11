#!/usr/bin/node
// Manage file in nodejs

const urlPath = 'http://swapi.co/api/films/' + process.argv[2];
const request = require('request');

request.get(urlPath, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const title = JSON.parse(body).title;
  console.log(title);
});
