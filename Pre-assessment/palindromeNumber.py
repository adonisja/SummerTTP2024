"""
    *   Name: palindromeNumber.py
    *   
    *   Define the function isPalindrome() that takes an integer argument and
    *   returns true if the number is a palindrome, and false otherwise.
    *   A palindrome is a number that reads the same forwards and backwards.
    *   For example, 121 is a palindrome, but 123 is not.
    *   Also, negative numbers cannot be palindromes.
    * 
    *   Constraints: Do not convert the integer to a string to solve this problem.
    *   Challenge: Try to solve this problem without allocating extra space.
    *   Hint: The numbers of digits in an integer can be calculated using:
    *   floor(log10(num)) + 1
"""
from math import log10, floor

def palindromeNumber(num):
    numDigits = floor(log10(num)) + 1 #finds the number length
    if num < 0:
        return False #Negative numbers cannot be palindromes
    if numDigits == 1:
        return True #Single digit numbers(0-9) are palindromes
    while numDigits > 1:
        fDigit = num // 10**(numDigits - 1)  #iterates over the first and last digits of the number
        lDigit = num % 10

        if fDigit != lDigit:  #returns false if these two digits are not the same
            return False

        num = (num % 10**(numDigits - 1)) // 10 # removes the first and last digit from the number
        numDigits -= 2 #reduces the length of the number by 2 after the first and last digits were removed

    return True


    
    
def main() -> None:
    num = int(input("Enter a Number: "))
    print(f'{num} is a palindrome') if palindromeNumber(num) else print(f'{num} is not a palindrome')
    
    
if __name__ == '__main__':
    main()