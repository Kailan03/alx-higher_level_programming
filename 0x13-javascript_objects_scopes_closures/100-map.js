#!/usr/bin/node

// Import the array
const list = require('./100-data');

// Compute the new array using map
const newList = list.map((value, index) => value * index);

// Print the initial list
console.log("Initial list:", list);

// Print the new list
console.log("New list:", newList);
