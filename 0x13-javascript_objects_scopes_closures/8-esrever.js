#!/usr/bin/node
// reverse the list
exports.esrever = function (list) {
  let myList = [];
  for (let index = list.length - 1; index >= 0; index--) {
    myList.push(list[index]);
  }
  return myList;
};
