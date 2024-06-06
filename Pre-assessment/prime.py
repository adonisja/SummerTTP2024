"""
    *   prime.py
    *   
    *   Define the function isPrime() that takes an integer argument and
    *   returns true if it is a prime number, false if it's not.
    *   A prime number is a number that is only divisible by 1 and itself.
    *   A prime number cannot be negative, 0, or 1.
"""
from math import isqrt # integer square root
def check(func):
    assert func(2) == True
    assert func(3) == True
    assert func(4) == False
    assert func(5) == True
    assert func(11) == True
    assert func(41) == True
    assert func(51) == False
    assert func(97) == True
    print("PASSED")
    return func

@check
def isPrime(num: int) -> bool:
    ...
    if num < 2:
        return False        #if the number is less than 2, automatically returns false
    for i in range(2, int(num**0.5) + 1):  # otherwise iterates over the range of 2 to the square root of the number + 1
        if num % i == 0:                   # if the number is divisible by the current count then returns false
            return False
    return True                   # if the loop completes successfully then the number is a prime and the function returns true
    

def main() -> None:
    ...
    print(isPrime(2)) # true
    print(isPrime(3)) # true
    print(isPrime(4)) # false
    print(isPrime(5)) # true
    print(isPrime(11)) # true
    print(isPrime(41)) # true
    print(isPrime(51)) # false
    print(isPrime(97)) # true

if __name__ == '__main__':
   main()