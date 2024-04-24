#!/usr/bin/node
// all characters of a Star Wars movie:
const req = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

req.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const con = JSON.parse(body);
    const characters = con.characters;
    
    for (const character of characters) {
      req.get(character, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const names = JSON.parse(body);
          console.log(names.name);
        }
      });
    }
  }
});
