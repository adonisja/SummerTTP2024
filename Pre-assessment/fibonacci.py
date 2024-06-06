def fibonacci(num):
    if num <= 1:
        return num     #base-case: returns the number entered if less than 2
    else:
        return fibonacci(num - 1) + fibonacci(num - 2) 
'''if the number is 2 or higher the function then returns
 a recursive function of 1 less than the current number added to two less than the current number
  e.g. if num = 3, it adds 2 + 1 '''
    
def main():
    num = int(input("Enter a number: "))
    print(f'Fibonacci Sequence of the first {num} numbers is: {fibonacci(num)}')

if __name__ == "__main__":
    main()
          