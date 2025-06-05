'''
Projeto de python para Global Solutions:
Simulação do funcionamento dos servidores, analise de dados e previsão de desastres
Baseado na media de leitura de um unico dispositivo

Grupo:
Guilherme Satler Macedo - RM 563330
Vitor Pallis - RM 561962
Miguel Manfre - RM 564233
'''

import random as r

## Valores constantes definidos durante o setup inicial do dispositivo
cord_dispositivo = ("29°54'20.2''S", "51°39'41.3''W") ## Valor definido pelo GPS
altitude = 33 ## Valor definido pelo Sensor de pressao atmosferica
rio_local = "Jacui" ## Valor definido pelo usuario ou adiquirido pelo dispositivo a partir da localizacao.

## Dados coletados pelo dispositivo ao longo do tempo
umidade_solo = [] ## % baseado na umidade do solo
temperatura = [] ## em Celsius

##Dados coletados pelo servidor atráves da internet ou outro sistema
previsao_chuva = [] ## chuva em mm
escoamento_do_rio = 0.5 ## escoamento constante do rio
nivel_rio_perigo = 2.1

## Previsão do servidor
previsao_nivel_rio_local = [] ## metros acima do nivel padrão

def previsao_elementos(i):
    '''
    A partir da diferenca dos valores dados pelos sensores, ele determina quais valores os outros dados deveriam ser para que a umidade do solo tenha conseguido chegar no valor dado.
    '''
    if umidade_solo[i] > umidade_solo[i-1] and i > 0:
        previsao_chuva.append(round(120*(umidade_solo[i]/(umidade_solo[i-1]+1)),2))
        previsao_chuva[i-1] = previsao_chuva[i]
        temperatura.append(round((temperatura[i-1] - (r.random()*3)),2))
    elif umidade_solo[i] < umidade_solo[i-1] and i > 0:
        previsao_chuva.append(0)
        temperatura.append(round((temperatura[i-1] + (r.random()*3)),2))
        if i == 1:
            previsao_chuva[i-1] = 0
    else:
        previsao_chuva.append(100.0)
        temperatura.append(23.5)

def previsao_rio(i):
    '''
    A partir da previsão de chuva, a Função determina quanto o nivel do rio deve subir ou descer.
    ''' 
    previsao_nivel_rio_local.append(0.2)
    if previsao_chuva[i] > 0 and i > 0:
        previsao_nivel_rio_local[i] = float(round(previsao_nivel_rio_local[i-1] + ((previsao_chuva[i]/500)*2),2))
    elif previsao_chuva[i] <= 0 and i > 0:
        previsao_nivel_rio_local[i] = float(round((previsao_nivel_rio_local[i-1] - escoamento_do_rio),2))
        if previsao_nivel_rio_local[i] < -0.5:
            previsao_nivel_rio_local[i] = -0.5

def receber_dados():
    '''
    Função para receber dados do dispostivo, porem nesta simulacao como input do usuario.
    '''
    try:
        us = (float(input("Insira a porcentagem da umidade do solo transmitido pelo dispositivo: ")))
        if 0 > us or us > 100:
            print("O valor precisa estar entre 0 e 100. Tente novamente:")
            return receber_dados()
        else:
            umidade_solo.append(us)
    except ValueError:
        print("Input Invalido. Tente novamente: ")
        return receber_dados()

def quantidade_de_dados():
    '''
    Função para definir a quantidade de dados a ser inserida no servidor. 
    No sistema real este sera um valor fixo, mas para o proposito de facilitar o uso da simulacao, este e um valor definido pelo usuario.
    '''
    try:
        x = int(input("Insira a quantidade de dados recebida: "))
        return x
    except ValueError:
        print("Input Invalido. Tente novamente: ")
        return quantidade_de_dados()
    
def exibir_dados():
    '''
    Função para exibir os dados para o usuario claramente.
    '''
    print(f"\nDados da Localizacao: {cord_dispositivo}.\n")
    for l in range(len(umidade_solo)):
        print(f"Dia {l+1}:\nUmidade do Solo: {umidade_solo[l]}%\nTemperatura: {temperatura[l]}°C\nPrevisão de chuvao: {previsao_chuva[l]} mm")
        alerta(l)
        
def alerta(l):
    if previsao_nivel_rio_local[l] > nivel_rio_perigo:
        print("\n********ALERTA*********\n")
        print(f"Enchente iminente!! Rio deve ultrapassar o nivel seguro de {nivel_rio_perigo}m\n")
        print(f"Previsão que o rio {rio_local} deve alcançar: {previsao_nivel_rio_local[l]}m")
        print("*****************************************************\n")
    else:
        print(f"Previsão que o rio {rio_local} deve alcançar: {previsao_nivel_rio_local[l]}m\n")

def main():
    '''
    Função principal que inicia todas as funcoes necessarias para o funcionamente da simulação.
    '''
    for i in range(quantidade_de_dados()):
        receber_dados()
        previsao_elementos(i)
        previsao_rio(i)    
    
    exibir_dados()
        
main()
