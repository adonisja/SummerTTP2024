def spam(v):
    sack = 0
    for i in v:
        sack += i
    return sack/len(v)

def smaller_than_average(v, average):
    small_nums = [] 
    print(average) 
    for i in v:
        if i < average:
            small_nums.append(i)
    print(f'Numbers smaller than the average are: {small_nums}')
    print(type(small_nums))

def main():
    v = [12, 8, 34, 19, 27]
    average = spam(v)
    smaller_than_average(v, average)

if __name__ == "__main__":
    main()