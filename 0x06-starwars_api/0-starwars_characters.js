#!/usr/bin/node
const request = require("request");

const movieId = process.argv[2];
if (!movieId) {
  console.error("Usage: ./0-starwars_characters.js <Movie ID>");
  process.exit(1);
}

const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    if (characters.length > 0) {
      printCharacters(characters, 0);
    } else {
      console.log("No characters found for this movie.");
    }
  } else {
    console.error(
      `Failed to fetch movie data. Status code: ${response.statusCode}`
    );
  }
});

function printCharacters(characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    if (response.statusCode === 200) {
      console.log(JSON.parse(body).name);
      printCharacters(characters, index + 1);
    } else {
      console.error(
        `Failed to fetch character data. Status code: ${response.statusCode}`
      );
    }
  });
}
