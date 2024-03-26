#!/usr/bin/node
const request = require('request');
const url = 'http://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, (err, response, body) => {
  if (err) {
    throw err;
  } else if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    const l = [];
    characters.forEach(character => {
      l.push(new Promise((resolve, reject) => {
        request.get(character, (err, response, body) => {
          if (err) {
            reject(err);
          } else if (response.statusCode === 200) {
            resolve(JSON.parse(body).name);
          }
        });
      }));
    });
    Promise.all(l).then(names => {
      names.forEach(name => console.log(name));
    });
  }
});
