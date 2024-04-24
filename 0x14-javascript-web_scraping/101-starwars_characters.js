#!/usr/bin/node
// all characters of a Star Wars movie:
const request = require('request');

// Extracting command line arguments
const [, , movieId] = process.argv;

// Function to retrieve characters from a movie
function getCharacters(movieId) {
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;
  
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }
    if (response.statusCode !== 200) {
      console.error('Status:', response.statusCode);
      return;
    }
    
    const film = JSON.parse(body);
    const characters = film.characters;
    
    // Fetch character names
    characters.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
          return;
        }
        if (response.statusCode !== 200) {
          console.error('Status:', response.statusCode);
          return;
        }
        
        const character = JSON.parse(body);
        console.log(character.name);
      });
    });
  });
}

// Call the function
getCharacters(movieId);

