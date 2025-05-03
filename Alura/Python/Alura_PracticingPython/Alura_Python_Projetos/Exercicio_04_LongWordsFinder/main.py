def find_long_words(text):
    words = text.split()
    long_words = []    
    for w in words:
        if len(w) > 10:
            long_words.append(w)
    return long_words

text = input("Insert your text: ")

long_words = find_long_words(text)

if long_words:
    print("Long words found:", ', '.join(long_words))
else:
    print("No long words found.")