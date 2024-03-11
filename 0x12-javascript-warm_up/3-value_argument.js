#!/usr/bin/node
const grap = process.argv.slice(2);
if (!grap[0]) {
  console.log('No argument');
} else {
  console.log(grap[0]);
}
