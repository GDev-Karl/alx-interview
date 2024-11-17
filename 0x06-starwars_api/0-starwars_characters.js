#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));

const filmID = process.argv[2];

if (!filmID) {
  console.error('Please provide a film ID');
  process.exit(1);
}

async function starwarsCharacters(filmId) {
  try {
    const endpoint = `https://swapi-api.hbtn.io/api/films/${filmId}`;
    let response = await request(endpoint);
    const filmData = JSON.parse(response.body);

    const characters = filmData.characters;

    for (const url of characters) {
      const charResponse = await request(url);
      const character = JSON.parse(charResponse.body);
      console.log(character.name);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
}

starwarsCharacters(filmID);
