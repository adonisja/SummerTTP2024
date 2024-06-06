"""
    *   Name: reverseArray.py
    *
    *   Given an list of integers, write a function that returns nothing,
    *   but reverses the order of the elements in the list.
    *   For example, if the list is [1, 2, 3, 4, 5, 6, 7, 8, 9],
    *   the function should modify the list to be [9, 8, 7, 6, 5, 4, 3, 2, 1].
    *   Constraints: Do not create another list, and do not use the built-in reverse() method.
    *   Hint: in python a, b = b, a assigns the value of b to a and the value of a to b.
"""
import runtime

def revArray(arr):
    a, b = 0, len(arr) - 1
    while a < b:
        arr[a], arr[b] = arr[b], arr[a]
        a, b = a + 1, b - 1
    

def main() -> None:
    ...
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Call your function with the arr list as an argument
    # Write your function call here
    revArray(arr)
    print("runtime")
    
    
    # Do not modify below this line
    print(arr)
    print(f"{arr == [9, 8, 7, 6, 5, 4, 3, 2, 1] = }")
if __name__ == '__main__':
    main()