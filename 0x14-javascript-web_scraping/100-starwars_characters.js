#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, (_err, _res, body) => {
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; i++) {
    request(characters[i], (_cErr, _cRes, cBody) => {
      console.log(JSON.parse(cBody).name);
    });
  }
});
