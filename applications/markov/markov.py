import random

with open("input.txt") as f:
    words = f.read()

words = words.split()

word_after = dict()

for i, word in enumerate(words[:-1]):
    if word in word_after:
        word_after[word].append(words[i+1])
    else: 
        word_after[word] = [words[i+1]]

sentence = "he"
value = sentence

while not sentence.endswith('.'):

    new_word = random.choice(word_after[value])
    sentence = sentence + ' ' + new_word
    value = new_word

print(sentence)

    

