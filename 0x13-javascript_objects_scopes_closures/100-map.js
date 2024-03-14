#!/usr/bin/node

// Import the filesystem module
const fs = require('fs');

// Read the content of the file
fs.readFile('./100-data.js', 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
    return;
  }

  // Parse the data as JSON
  const list = JSON.parse(data);

  // Compute the new array using map
  const newList = list.map((value, index) => value * index);

  // Print the initial list
  console.log("Initial list:", list);

  // Print the new list
  console.log("New list:", newList);
});
