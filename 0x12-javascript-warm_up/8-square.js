#!/usr/bin/node

let size = process.argv[2];
if (isNaN(size)) {
  console.log('Missing size');
}
size = parseInt(size);
let row = '';
for (let i = size; i > 0; i--) {
  row += 'X';
}
for (size; size > 0; size--) {
  console.log(row);
}
