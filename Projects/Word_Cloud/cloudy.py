import wordcloud
from matplotlib import pyplot as plt
import re, string

# Read the input file
file_contents = open("Projects/Word_Cloud/AnimalFarm.txt", "r").read()

# Create a list of words from the input text
input_words = file_contents.split()

# Display the first 100 words in the list
print("=== WORDS ===")
print(input_words[:100])

# Very common words should be removed from input_words, so that they don't show up on the word cloud, so let's define a list of common words to remove
stop_words = ['one', 'two', 'said', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'can', 'could', "couldn't", 'get', 'got', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", 'around', 'back', 'front', 'like', 'would', 'something', 'someone', 'somewhere', 'that', 'there', 'these', 'nothing' 'nowhere', 'everywhere', 'everyone', 'everything', 'anything', 'everybody' 'everyone', 'everything', 'anybody', 'anyone', 'anything', 'anywhere', 'anytime', 'anyway', 'anyhow', 'anyplace', 'go', 'come', 'make', 'went', 'came', 'made', 'do', 'done', 'get', 'got', 'gone', 'know', 'knew', 'take', 'took', 'see', 'saw', 'seem', 'seen', 'come', 'came', 'go', 'gone', 'seeing', 'going', 'doing', 'coming', 'taking', 'knowing', 'making']


''' Complete the following line using a list comprehension to convert all the words in input_words to lower case and exclude the words that have characters that are not letters. 
  
  >> Use the String function lower(), which converts a string to lower cases. See https://www.w3schools.com/python/ref_string_lower.asp
  
  >> Use the String function isalpha(), which returns True if all the characters in a string are alphabet letters (a-z). See https://www.w3schools.com/python/ref_string_isalpha.asp 
'''


words_alpha = [word for word in input_words if word.isalpha()]


''' Complete the following line using a list comprehension to remove the stop_words from from words_alpha '''
final_words = [word for word in words_alpha if word not in stop_words]


''' Complete the following line using a dictionary comprehension to create a dictionary with the frequencies of each word in the list final_words. For example, given the following final_words list:

  ['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 'cherry']

  the result should be:

  {'apple': 3, 'banana': 2, 'orange': 1, 'cherry': 1}}

  >> Use the List function count(target) which returns the number of times the target value appears on the list. See https://www.w3schools.com/python/ref_list_count.asp
'''
freqs_final_words = {word: final_words.count(word) for word in set(final_words)}


# Prints the first 100 entries in the dictionary
print("=== FINAL WORDS FREQS ===")
print (dict(list(freqs_final_words.items())[0: 100]))


# GENERATE A WORD CLOUD FROM THE FINAL WORDS FREQUENCIES (freqs_final_words)
#cloud = wordcloud.WordCloud.generate(words_alpha)

cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(freqs_final_words)
my_image = cloud.to_array()
plt.imshow(cloud, interpolation='nearest')
plt.axis('off')
plt.show()