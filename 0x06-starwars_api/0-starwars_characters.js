#!/usr/bin/node

const request = require('request');

// Ensure a movie ID is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Fetch the movie details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to retrieve data. Status code: ${response.statusCode}`);
    return;
  }

  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;

  // Helper function to fetch and print character names sequentially
  const fetchCharacterNames = (index) => {
    if (index >= characterUrls.length) return;

    request(characterUrls[index], (err, res, charBody) => {
      if (err) {
        console.error('Error fetching character data:', err);
        return;
      }

      if (res.statusCode !== 200) {
        console.error(`Failed to retrieve character. Status code: ${res.statusCode}`);
        return;
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);

      // Fetch the next character
      fetchCharacterNames(index + 1);
    });
  };

  // Start fetching characters
  fetchCharacterNames(0);
});
