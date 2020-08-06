with open("robin.txt") as f:
    words = f.read()

words = words.split()

word_dict = dict()

for word in words:
    word = word.lower()

    characters = """:;,."-+=/\|[]{}()*^&"""
    for c in characters:
       word = word.replace(c, '')

    if word not in word_dict:
        word_dict[word] = 0
    word_dict[word] += 1

words = list(word_dict.items())
words.sort()
words.sort(key=lambda x: x[1], reverse=True)

for word in words:
    print(word[0] + " " * (15 - len(word[0])) + "#" * word[1])
    

