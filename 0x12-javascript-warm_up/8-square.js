#!/usr/bin/node
const argv = process.argv;
const x = parseInt(argv[2]);
const character = 'X';
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let j = 0; j < x; j++) {
    console.log(character.repeat(x));
  }
}
