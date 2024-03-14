#!/usr/bin/node

// Define the function converter
exports.converter = function (base) {
  // Recursive function to convert number to specified base
  return function convert (num) {
    // Base case: if num is 0, return '0'
    if (num === 0) {
      return '0';
    }
    // Otherwise, convert the number to the specified base
    let result = '';
    while (num > 0) {
      result = '0123456789abcdefghijklmnopqrstuvwxyz'.charAt(num % base) + result;
      num = Math.floor(num / base);
    }
    return result;
  };
};
