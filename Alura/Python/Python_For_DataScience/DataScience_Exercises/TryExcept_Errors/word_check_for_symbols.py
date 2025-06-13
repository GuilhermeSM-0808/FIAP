## Exxercicio 6

## Given lists by exercise to be tested
clean_list = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',
                  'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']

dirty_list = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil',
                  'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']

## My code -->

symbols_to_check_for = [',','.','!','?']

def check_for_symbol(symbols, list_of_words):
    for word in list_of_words:
        for s in symbols:
            if s in word:
                raise ValueError(f"The text present a symbol on the word: {word}")
    print("Full list checked. No Symbols found.")
    
try:
    check_for_symbol(symbols_to_check_for, dirty_list)
except ValueError as e:
    print("Error:", e)