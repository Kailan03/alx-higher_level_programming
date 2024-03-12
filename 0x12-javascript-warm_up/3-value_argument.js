#!/usr/bin/node

// Get the first argument
const arg = process.argv[2];

// Check if an argument is provided
if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
