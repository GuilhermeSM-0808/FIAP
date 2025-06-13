## Exercicio 4 -- https://cursos.alura.com.br/course/python-data-science-funcoes-estruturas-dados-excecoes/task/126473

#testing variables
list1 = [4,6,7,9,10,20]
list2 = [-4,6,8,7,9]

def juntar(list1,list2):
    new_list = []
    if len(list1) != len(list2):
        raise IndexError
    else:
        for i in range(len(list1)):
            tupla = (list1[i],list2[i],(list1[i]+list2[i]))
            new_list.append(tupla)
        return new_list
    
    
try:
    result = juntar(list1,list2)
    print(result)
except IndexError:
    print("Error: Lists are of different lengths.")
except TypeError:
    print("Error: Invalid variable type found in lists.")