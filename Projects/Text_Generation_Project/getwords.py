import random

def getwords(fileName):
  file = open(fileName, 'r')
  text = file.read()
  print(text)
  stopletters = [".", ",", ";", ":", "'s", '"', "!", "?", "(", ")", '“', '”']
  text = text.lower()
  for letter in stopletters:
    text = text.replace(letter, "")
  words = text.split()
  return words

getwords("/workspaces/SummerTTP2024/Projects/Text_Generation_Project/sample.txt")

def compute_bigrams(fileName):
  input_list = getwords(fileName)
  bigram_list = {}
  for i in range(len(input_list)-1):
    if input_list[i] in bigram_list:
      bigram_list[input_list[i]] = bigram_list[input_list[i]]+[input_list[i+1]]
    else:
      bigram_list[input_list[i]] = [input_list[i+1]]
  return bigram_list
