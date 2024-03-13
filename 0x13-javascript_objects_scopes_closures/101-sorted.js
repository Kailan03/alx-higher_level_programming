#!/usr/bin/node

// Import the dictionary
const dict = require('./101-data');

// Compute the new dictionary
const newDict = {};

// Iterate over the original dictionary
for (const key in dict) {
  const occurrences = dict[key];
  if (occurrences.length in newDict) {
    newDict[occurrences.length].push(...occurrences);
  } else {
    newDict[occurrences.length] = occurrences;
  }
}

// Print the new dictionary
console.log(newDict);
