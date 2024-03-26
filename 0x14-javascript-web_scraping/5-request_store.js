#!/usr/bin/node

const url = process.argv[2];
const path = process.argv[3];
const fs = require('fs');
const request = require('request');

request(url, (err, data, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(path, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
