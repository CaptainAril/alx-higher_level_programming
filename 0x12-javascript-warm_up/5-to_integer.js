#!/usr/bin/node

import { argv } from 'node:process';

const value = argv[2];
if (isNaN(value)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(value)}`);
}
