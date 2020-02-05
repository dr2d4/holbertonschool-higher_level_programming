#!/usr/bin/node

const n = process.argv[2];

if (!n) {
  console.log('Missing number of occurrences');
} else {
  for (let i = n; i > 0; i--) {
    console.log('C is fun');
  }
}
