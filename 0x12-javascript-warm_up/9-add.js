#!/usr/bin/node

// Define the function add
function add (a, b) {
  return a + b;
}

// Get the two integers from command line arguments
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

// Check if both arguments are integers
if (!isNaN(num1) && !isNaN(num2)) {
  // Print the addition of the two integers
  console.log(add(num1, num2));
} else {
  console.log('no argument');
}
