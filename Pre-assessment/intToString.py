def intToString(num: int) -> str:
    istring = ''  #creates a string holder variable
    isNeg = False   #intializes a bool variable to check for negative numbers
    if num < 0:
        isNeg = True        #if the number is neg, sets the bool to negative and removes the - sign
        num = -num
    if num  == 0:       # if the number is 0, a string variable 0 is returned
        return '0'
    while num > 0:                                      # while the number is greater than 0, it will loop through the number
        istring = chr((num % 10) + 48) + istring        # one character at a time, converts into into a character 
        num = num // 10                                 # and then concatenates it to the string
                                                        # the last digit is then removed from num

    if isNeg:                                                   # if the num was negative, 
        print(f'istring: {istring}, type: {type(istring)}')     # a negative sign is added to the front of the string
        return '-' + istring

    return istring
    
    
def main() -> None:
    print(intToString(123)) # Expected output: "123"
    print(intToString(-123)) # Expected output: "-123"
    print(intToString(0)) # Expected output: "0
    print(intToString(123456789)) # Expected output: "123456789"
    
if __name__ == "__main__":
    main()