#!/usr/bin/node

// Get number of arguments
const numArgs = process.argv.length - 2;

// Print message depending on the number of arguments
if (numArgs === 0) {
  console.log('No argument');
} else if (numArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
