#!/usr/bin/node
// ontents of a webpage

const req = require('request');
const fsy = require('fs');

req.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fsy.writeFile(process.argv[3], body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
