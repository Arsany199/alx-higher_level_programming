#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let x = 0;

request(url, (err, data, body) => {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body).results;
    for (let i = 0; i < body.lenth; i++) {
      const characters = films[i].characters;

      for (let j = 0; j < characters.lenth; j++) {
        if (characters[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
          x = x + 1;
        }
      }
    }
    console.log(x);
  }
});
