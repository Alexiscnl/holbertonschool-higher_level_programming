#!/usr/bin/node

const argv2 = process.argv[2];
const num = 'X'.repeat(argv2);

if (isNaN(parseInt(argv2))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argv2; i++) {
    console.log(num);
  }
}
