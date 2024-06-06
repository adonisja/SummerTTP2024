num = int(input("Enter a number: "))
if num < 2:
        print(False)
for i in range(2, int(num**0.5) + 1):
        print(f'Current Count: {i}, wMax Range:{int(num**0.5)+1}')
        if num % i == 0:
                print(False)
                break
        
print(True)