#!/usr/bin/node

const a = process.argv.slice(2);

if (!a.length || a.length === 1) {
  console.log('0');
} else {
  console.log(a.sort().reverse()[1]);
}
