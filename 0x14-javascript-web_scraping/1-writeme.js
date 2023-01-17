#!/usr/bin/node

const fs = require('fs');

const fileName = process.argv[2];
const string = process.argv[3];

fs.writeFile(fileName, string, 'utf8', (err) => {
  if (err)
    console.log(err);
})