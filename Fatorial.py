"""Faça uma funçao recursiva que retorne o fatorial de um numero"""
# O que é um fator: 5: 5 * 4 * 3 * 2 * 1 
# fator_x = 5 * (5-1) até 
def fatorial(n):
    if n == 1 or n==0:
        return 1
    else:
        return n * fatorial(n-1)


numero = int(input("Digite um numero:"))    
resultado = fatorial(numero)
print(resultado)




    