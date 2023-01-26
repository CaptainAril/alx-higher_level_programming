#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request.get(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    const users = JSON.parse(body);
    const obj = {};
    let id = 0;
    let count = 0;
    for (const user of users) {
      if (id < user.userId) {
        id = user.userId;
        count = 0;
        if (obj[id]) {
          count = obj[id];
        } 
      }
      if (user.userId === id && user.completed === true) {
        count++;
        obj[id] = count;
      }
    }
    console.log(obj);
  }
});
