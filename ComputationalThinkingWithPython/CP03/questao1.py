palavras = []

def quantasLetras(palavra):
    quantidades = {}
    print(f"A palavra '{palavra}' possui:")
    for letra in palavra:
        if letra in quantidades:
            quantidades[letra] += 1
        else:
            quantidades[letra] = 1
    for q in quantidades:
        print(f"{q}:{quantidades[q]}")

for i in range(3):

    palavra = str(input(f"Insira a palavra N°{i+1}: ").lower())
    palavras.append(palavra)

for p in palavras:
    quantasLetras(p)

# O programa pede ao usuario por 3 strings e retorna para o usuario a palavra seguida por uma lista indicando a quantidade de cada letra na palavra.
# Ele faz a contagem das letras, colocando as palavras em uma lista, depois os itens da lista são iterados em uma função, onde as letras dos itens são colocadas em um dicionario local (variavel local), caso a letra já exista no dicionario, ele simplesmente aumenta a quantidade marcada dentro do dicionario. E depois essa função exibe esses valores ao usuario através do print (novamente iterando por cada item do dicionario). E como o dicionario é local, esse valores são apagados quando a função é executada novamente com a próxima palavra da lista.