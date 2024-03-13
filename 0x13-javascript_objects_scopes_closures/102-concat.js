#!/usr/bin/node

// Import required module
const fs = require('fs');

// Get file paths from command line arguments
const file1Path = process.argv[2];
const file2Path = process.argv[3];
const destinationPath = process.argv[4];

// Read the content of the first file
fs.readFile(file1Path, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading ${file1Path}:`, err);
    return;
  }

  // Read the content of the second file
  fs.readFile(file2Path, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading ${file2Path}:`, err);
      return;
    }

    // Concatenate the content of the two files
    const concatenatedData = data1 + data2;

    // Write the concatenated data to the destination file
    fs.writeFile(destinationPath, concatenatedData, 'utf8', (err) => {
      if (err) {
        console.error(`Error writing to ${destinationPath}:`, err);
        return;
      }
      console.log(`Concatenated data has been written to ${destinationPath}`);
    });
  });
});
