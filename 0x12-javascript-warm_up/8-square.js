#!/usr/bin/node

// Get the size of the square from the first argument
const size = parseInt(process.argv[2]);

// Check if the argument can be converted to an integer
if (!isNaN(size)) {
  // Loop to print each row of the square
  for (let i = 0; i < size; i++) {
    let row = '';
    // Loop to print each column of the square
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
