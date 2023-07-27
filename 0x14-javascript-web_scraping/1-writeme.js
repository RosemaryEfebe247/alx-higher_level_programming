#!/usr/bin/node
const file_sys = require('fs');
file_sys.writeFile(process.argv[2], process.argv[3], 'utf8', (err) => {
	if (err) console.error(err);
});
