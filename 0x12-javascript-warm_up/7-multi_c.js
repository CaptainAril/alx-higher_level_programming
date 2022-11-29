#!/usr/bin/node

let val = process.argv[2];
if (isNaN(val)) {
  console.log('Missing number of occurrences');
}
val = parseInt(val);
for (val; val > 0; val--) {
  console.log('C is fun');
}
