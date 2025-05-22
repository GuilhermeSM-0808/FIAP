def custoProducao(custo,quantidade):
    custo_total = custo * quantidade
    return custo_total

try:
    nome = str(input("Insira o nome do produto: "))
    if nome != '':
        custo = float(input("Insira o custo de produção por peça: "))
        quantidade = int(input("Insira a quantidade de peças a ser produzidas: "))
        custo_total = custoProducao(custo,quantidade)
        print(f"A produção da peça: {nome} custara R${custo_total:.2f} para ser concluida.")
    else:
        print("Nome não poder ser vazio...")

except:
    print("ERRO: Valor inserido invalido.")

#O programa pede ao usuario o nome da peça, o custo para produzir cada peça (como float) e a quantidade a ser produzida (como int). Retornando ao usuario o custo da produção total daquela peça. Caso o input do nome esteja vazio ou qualquer input do usuario do sejá invalido, o programa retorna um aviso/erro e encerra o programa.