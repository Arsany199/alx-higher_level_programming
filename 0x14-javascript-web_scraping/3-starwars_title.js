#!/usr/bin/node

const request = require('request');
const urlintask = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(urlintask, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(body && JSON.parse(body).title);
  }
});
