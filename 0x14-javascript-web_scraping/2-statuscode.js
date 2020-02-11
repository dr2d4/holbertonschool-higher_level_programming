#!/usr/bin/node
// Manage file in nodejs

const request = require('request');
const file = process.argv[2];

request.get(file).on('response', res => console.log('code: ' + res.statusCode));
