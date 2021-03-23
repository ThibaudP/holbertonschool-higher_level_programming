#!/usr/bin/node
// Reads fileA and fileB & concatenate their content to fileC
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const textA = fs.readFileSync(fileA);
const textB = fs.readFileSync(fileB);

fs.writeFileSync(fileC, textA + textB);
