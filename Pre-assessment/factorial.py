def factorial(num):
    if num == 0 or num == 1: #base-case: checks if the number is 0 or 1
        return 1             #if True, then returns 1
    else:                    
        return factorial(num - 1) * num    #if False, runs a recursive function


def main():
    print(factorial(0)) # 1
    print(factorial(1)) # 1
    print(factorial(3)) # 6
    print(factorial(5)) # 120
    print(factorial(10)) # 3628800


if __name__ == "__main__":
    main()