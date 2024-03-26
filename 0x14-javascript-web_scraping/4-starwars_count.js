#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, data, body) => {
  if (err) {
    console.log(err);
  } else {
    let x = 0;
    const films = JSON.parse(body).results;
    for (let i = 0; i < films.length; i++) {
      const characters = films[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j] === 'https://swapi-api.hbtn.io/api/people/18/' || characters[j] === 'http://swapi-api.hbtn.io/api/people/18/') {
          x += 1;
        }
      }
    }
    console.log(x);
  }
});
