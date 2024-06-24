from getwords import compute_bigrams

import random

def main():
    two_grams = compute_bigrams("Projects/Text_Generation_Project/sample.txt")
    print(two_grams)
    chosen = random.choice(list(two_grams.keys()))
    print(chosen)
    for i in range(50):
        words = two_grams[chosen] #list of words with key=chosen from two_grams
        chosen = random.choice(words) #random choice from words
        print(chosen, end=" ")


    

if __name__ == "__main__":
    main()