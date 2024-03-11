#!/usr/bin/node
const add = (a, b) => parseInt(a) + parseInt(b);
const in1 = process.argv[2];
const in2 = process.argv[3];
const res = add(in1, in2);
console.log(res);
