## Codigo Inicial

# frase = input("Digite uma frase: ")
# palavras = frase.split()
# print(len(palavras))
# print(palavras)

from contador import contar_palavras

frase = input("Digite uma frase: ").strip()
if not frase:
    print("Erro: Nenhuma frase foi inserida.")
else:
    resultado = contar_palavras(frase)
    if resultado:
        print("Contagem de Palavras: ")
        for palavra, quantidade in resultado.items():
            print(f"{palavra}:{quantidade}")
    else:
        print(f"Nenhuma palavra valid[a foi encontrada.")