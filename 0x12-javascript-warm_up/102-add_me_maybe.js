#!/usr/bin/node
// print 2 addition of ints
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
