#!/usr/bin/node

// Get the first argument
const arg = process.argv[2];

// Convert the argument to an integer
const num = parseInt(arg);

// Check if the argument can be converted to an integer
if (!isNaN(num)) {
  // Loop to print "C is fun" x times
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
