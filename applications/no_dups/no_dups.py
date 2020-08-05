def no_dups(s):
    
    words = s.split()

    word_dict = dict()

    if words:
        for word in words:
            if word not in word_dict:
                word_dict[word] = True
    else:
        return ""

    return " ".join(list(word_dict.keys()))

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))