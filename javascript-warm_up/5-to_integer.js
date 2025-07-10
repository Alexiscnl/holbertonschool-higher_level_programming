#!/usr/bin/node
const argv2 = process.argv[2];
if (!isNaN(parseInt(argv2))) {
	console.log('My number: ' + parseInt(argv2));
}else {
	console.log('Not a number');
}
