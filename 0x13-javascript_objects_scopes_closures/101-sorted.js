#!/usr/bin/node
// script that imports a dictionary of occurrences by user id
const dict = require('./101-data.js').dict;
let nDict = {};
for (let key in dict) {
  if (nDict[dict[key]] === undefined) {
    nDict[dict[key]] = [key];
  } else {
    nDict[dict[key]].push(key);
  }
}
console.log(nDict);
