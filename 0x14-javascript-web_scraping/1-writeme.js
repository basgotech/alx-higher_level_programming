#!/usr/bin/node
//  script that writes a string to a file.

const fs = require('fs');

// Extracting command line arguments
const [, , filePath, content] = process.argv;

// Write content to file
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
});
