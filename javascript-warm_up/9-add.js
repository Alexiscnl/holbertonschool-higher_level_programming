#!/usr/bin/node
const argv2 = parseInt(process.argv[2]);
const argv3 = parseInt(process.argv[3]);

if (isNaN(argv2) || isNaN(argv3)) {
  console.log('NaN');
} else {
  console.log(argv2 + argv3);
}
