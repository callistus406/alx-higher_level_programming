#!/usr/bin/node

const numArgs = parseInt(process.argv[2]);

if (isNaN(numArgs)) {
  console.log("Missing number of occurrences");
} else {
  let i = 0;
  while (i < numArgs) {
    console.log("C is fun");
    i++;
  }
}
