#!/usr/bin/node

// Define the factorial function recursively
function factorial(n) {
  // Base case: factorial of 0 or NaN is 1
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    // Recursive case: factorial of n is n multiplied by factorial of (n-1)
    return n * factorial(n - 1);
  }
}

// Get the integer from the first argument
const num = parseInt(process.argv[2]);

// Compute the factorial and print the result
console.log(factorial(num));

