#!/usr/bin/node

const n = process.argv[2];

if (!parseInt(n)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${n}`);
}
