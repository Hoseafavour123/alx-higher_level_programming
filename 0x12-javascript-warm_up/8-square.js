#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (isNaN(size) || process.argv[2] === 'undefined') {
  console.log('Missing size');
}

if (size > 0) {
  let mark = 'X';
  for (let i = 0; i < size - 1; i++) {
    mark += 'X';
  }

  for (let j = 0; j < size; j++) {
    console.log(mark);
  }
}
