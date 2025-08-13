def fatorial(n):
    if n == 0:
        return 1
    return n*fatorial(n-1)

def soma(lista):
    return sum(lista)

def media(lista):
    return soma(lista) / len(lista)

nums = [100, 200, 300, 400, 500]

print(soma(nums))
print(media(nums))