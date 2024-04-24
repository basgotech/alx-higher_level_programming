#!/usr/bin/node
// Return Number of films 
const req = require('request');
let count = 0;

req.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const con = JSON.parse(body);
    con.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
