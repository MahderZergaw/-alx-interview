#!/usr/bin/node

const request = require('request');

async function getMovieCharacters (movieId) {
  return new Promise((resolve, reject) => {
    request(`https://swapi.dev/api/films/${movieId}/`, (error, response, body) => {
      if (error) {
        console.error(`Error fetching movie data for Movie ID ${movieId}: ${error.message}`);
        reject(new Error(`Error fetching movie data for Movie ID ${movieId}`));
      } else {
        const movieData = JSON.parse(body);
        const characters = movieData.characters;

        Promise.all(characters.map((characterUrl) => {
          return new Promise((resolveChar, rejectChar) => {
            request(characterUrl, (charError, charResponse, charBody) => {
              if (charError) {
                rejectChar(new Error(`Error fetching character data for URL ${characterUrl}`));
              } else {
                const characterData = JSON.parse(charBody);
                resolveChar(characterData.name);
              }
            });
          });
        })).then((characterNames) => {
          resolve(characterNames);
        }).catch((err) => {
          reject(err);
        });
      }
    });
  });
}

async function main () {
  if (process.argv.length !== 3) {
    console.log('Usage: node 0-starwars_characters.js <Movie ID>');
    process.exit(1);
  }

  const movieId = parseInt(process.argv[2]);
  const characterNames = await getMovieCharacters(movieId);
  characterNames.forEach((name) => console.log(name));
}

main();