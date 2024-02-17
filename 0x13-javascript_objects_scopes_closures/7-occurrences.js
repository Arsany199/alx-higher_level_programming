#!/usr/bin/node
// returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  for (let index = 0; index < list.length; index++) {
    if (list[index] === searchElement) {
      i++;
    }
  }
  return i;
};
