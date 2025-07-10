#!/usr/bin/node
const nbArgv = process.argv.length - 2;

if (nbArgv === 0) {
  console.log('No argument');
} else if (nbArgv === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
