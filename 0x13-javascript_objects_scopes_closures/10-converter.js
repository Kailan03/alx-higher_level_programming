#!/usr/bin/node

// Define the function converter
exports.converter = function(base) {
  // Recursive function to convert number to specified base
  return function convert(num) {
    // Base case: if num is 0, return an empty string
    return num === 0 ? '' : convert(Math.floor(num / base)) + '0123456789abcdefghijklmnopqrstuvwxyz'.charAt(num % base);
  }
}
