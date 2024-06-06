from sys import argv
import time
 

def runtime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start:.5f} seconds")
    return wrapper

@runtime
def main() -> None:
    ...
    print("Hello, World!")

if __name__ == '__main__':
    main()