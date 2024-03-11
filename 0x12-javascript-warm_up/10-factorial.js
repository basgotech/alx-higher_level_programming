#!/usr/bin/node
const factorial = (inn) => {
  if (isNaN(inn)) {
    return 1;
  }
  inn = parseInt(inn);
  if (inn <= 1) {
    return 1;
  }
  return inn * factorial(inn - 1);
};
const cin = process.argv[2];
const cout = factorial(cin);
console.log(cout);
