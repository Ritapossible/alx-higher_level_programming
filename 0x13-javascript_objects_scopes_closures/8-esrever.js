#!/usr/bin/node
exports.esrever = function (list) {
  const newlist = [];
  for (let j = list.length - 1; j >= 0; j--) {
    newlist.push(list[j]);
  }
  return newlist;
};
