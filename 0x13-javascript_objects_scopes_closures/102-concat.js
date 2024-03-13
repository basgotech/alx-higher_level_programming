#!/usr/bin/node
const fs = require('fs');
const gh = fs.readFileSync(process.argv[2]).toString();
const fg = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], gh + fg);
