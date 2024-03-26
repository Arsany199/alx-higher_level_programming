#!/usr/bin/node

const request = require('request');
const myurl = process.argv[2];

request(myurl, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ', response.statusCode);
  }
});
