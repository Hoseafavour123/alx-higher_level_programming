#!/usr/bin/node

const myVar = parseInt(process.argv[2]);

if (process.argv[2] === 'undefined' || isNaN(myVar)) {
  console.log('Missing number of occurences');
} else if (myVar > 0) {
  let i = 0;
  while (i < myVar) {
    console.log('C is fun');
    i++;
  }
}
