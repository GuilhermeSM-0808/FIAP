def count_vowels(text):
    text = text.lower()
    amount_vowels = 0

    for letter in text:
        if letter in "aeiouy":
            amount_vowels += 1
    return amount_vowels
        
text = input("Insert your text: ")

print(f"The text contains {count_vowels(text)} vowels")