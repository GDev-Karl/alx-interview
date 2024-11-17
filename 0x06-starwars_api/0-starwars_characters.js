#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

if (!movieId) {
  console.log('Please provide a movie ID');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching the movie:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.log(`Failed to fetch movie data. Status code: ${response.statusCode}`);
    return;
  }

  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  // For each character URL, fetch and print the name
  characterUrls.forEach((url) => {
    request(url, (error, response, body) => {
      if (error) {
        console.error('Error fetching character:', error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
