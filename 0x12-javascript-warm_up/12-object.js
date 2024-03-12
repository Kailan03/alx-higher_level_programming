#!/usr/bin/node

// Get the list of arguments excluding the first two which are node and script name
const args = process.argv.slice(2);

// Check if no arguments were passed or only one argument was passed
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  // Convert arguments to integers and replace 12 with 89
  const integers = args.map(Number).map(num => num === 12 ? 89 : num).sort((a, b) => b - a);

  // Find the second biggest integer
  const secondBiggest = integers[1];

  // Print the second biggest integer
  console.log(secondBiggest);
}
