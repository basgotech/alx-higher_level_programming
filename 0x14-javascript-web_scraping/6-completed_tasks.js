#!/usr/bin/node
// tasks completed by user id.

const req = require('request');

req.get(process.argv[2], { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const ts = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!ts[todo.userId]) {
        ts[todo.userId] = 1;
      } else {
        ts[todo.userId] += 1;
      }
    }
  });
  console.log(ts);
});
