#!/usr/bin/node
const count = process.argv.length - 2;

if (count == 0) {
	console.log('No argument');
}

else if (count == 1) {
	console.log('Argument found');
}

else {
	console.log('Arguments found');
}
