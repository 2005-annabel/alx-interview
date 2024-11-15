#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const filmEndPoint = 'https://swapi-api.hbtn.io/api/films/' + movieId;
let people = [];
const names = [];

const requestCharacters = async () => {
  await new Promise(resolve => {
    request(filmEndPoint, (err, res, body) => {
      if (err || res.statusCode !== 200) {
        console.error('Error fetching film data:', err || res.statusCode);
      } else {
        const jsonBody = JSON.parse(body);
        people = jsonBody.characters;
      }
      resolve();
    });
  });
};

const requestNames = async () => {
  for (const p of people) {
    await new Promise(resolve => {
      request(p, (err, res, body) => {
        if (err || res.statusCode !== 200) {
          console.error('Error fetching character data:', err || res.statusCode);
        } else {
          const jsonBody = JSON.parse(body);
          names.push(jsonBody.name);
        }
        resolve();
      });
    });
  }
};

const getCharNames = async () => {
  await requestCharacters();
  await requestNames();

  for (let i = 0; i < names.length; i++) {
    process.stdout.write(names[i] + (i < names.length - 1 ? '\n' : ''));
  }
};

getCharNames();
