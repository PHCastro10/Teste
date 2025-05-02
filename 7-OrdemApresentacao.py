#Esse programa consiste em sortear a ordem de apresentação do grupo
from random import shuffle

participantes = []
i = 1

print("Digite os nomes que irão participar da apresentação (Digite 0 ou sair para encerrar):")

while True:
    participante = (input(f"Participante {i}: ")).strip()
    if (participante == "0") or (participante.lower()) == "sair":
        break
    participantes.append(participante)
    i += 1
    
shuffle(participantes)

print("A nova orde he: ")
print(participantes)
    



