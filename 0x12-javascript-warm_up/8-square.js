#!/usr/bin/node
const sg = parseInt(process.argv[2]);
if (!isNaN(sg) && sg > 0) {
  for (let i = 0; i < sg; i++) {
    console.log('X'.repeat(sg));
  }
} else {
  console.log('Missing size');
}
