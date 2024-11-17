#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  if (res.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    // Fetch and print character names in order
    fetchCharactersInOrder(characters, 0);
  } else {
    console.error(`Failed to retrieve movie data. Status code: ${res.statusCode}`);
  }
});

function fetchCharactersInOrder(characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], (err, res, body) => {
    if (err) {
      console.error(err);
      return;
    }

    if (res.statusCode === 200) {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      fetchCharactersInOrder(characters, index + 1);
    } else {
      console.error(`Failed to retrieve character data. Status code: ${res.statusCode}`);
    }
  });
}
