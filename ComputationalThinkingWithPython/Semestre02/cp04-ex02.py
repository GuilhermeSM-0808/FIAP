clima = {}

def inserir_dados(cidade):
    temp = float(input(f"Insira a temperatura de {cidade}: "))
    umi = float(input(f"Insira a Umidade de {cidade}: "))
    cond = input(f"Insira a condição do clima de {cidade}: ")
    return temp, umi, cond

def inserir_cidade(i):
    nome = input(f"Insira o nome da cidade {i+1}: ")
    temp, umi, cond = inserir_dados(nome)
    clima[nome] = {'Temperatura': temp, 'Umidade': umi, 'Condição': cond}

def alterar_dados():
    lista_cidades = []
    for cidade in clima.keys():
        lista_cidades.append(cidade)

    clima[lista_cidades[0]]['Condição'] = input(f"Altere a condição do clima de {lista_cidades[0]}: ")
    clima[lista_cidades[1]]['Umidade'] = input(f"Altere a umidade de {lista_cidades[1]}: ")
    clima[lista_cidades[2]]['Temperatura'] = input(f"Altere a temperatura de {lista_cidades[2]}: ")


def main():
    for i in range(3):
        inserir_cidade(i)

    print("\n ---------- Dados ---------")
    print(clima)
    print('\n')

    alterar_dados()

    print('\n-------- Dados Alterados ----------')
    print(clima)
    print('\n')

try:
    main()
except:
    print("Input Invalido. Terminando programa.")
    exit()