#!/usr/bin/node

const args = process.argv;
function add(a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  } else {
    return a + b;
  }
}

console.log(add(parseInt(args[2]), parseInt(args[3])));
