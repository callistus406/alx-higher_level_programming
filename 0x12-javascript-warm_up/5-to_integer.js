#!/usr/bin/node
const convertToInt = process.argv[2];
if (isNaN(convertToInt)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${convertToInt}`);
}
