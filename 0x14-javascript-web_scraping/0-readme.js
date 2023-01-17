#!/usr/bin/node
// Reads file

const fs = require('fs')
const fileName = process.argv[2]

fs.readFile(fileName, 'utf-8', function (error, data) {
  console.log(error || data)
})
