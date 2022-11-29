#!/usr/bin/node

const sortedArray = process.argv.slice(2).sort((a, b) => a - b);
const val = sortedArray[sortedArray.length - 2];
console.log(isNaN(val) ? 0 : val);
