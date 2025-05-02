fruta = ["maçã", "banana", "melancia"]

for elemento in fruta:  #imprimindo as frutas da lista
        print(elemento, end=" ")

print()  
fruta.append("mamão") #adiciona mais um elemento na lista, no final dela
fruta.insert(0,"abacate") # adiciona um elemento no indici fornecido
fruta.remove ("banana") #remove o elemento
fruta.pop(1) #remove o indici

for elemento in fruta:  #imprimindo as frutas da lista
    print(elemento, end=" ")
print()

print("O tamanho da lista he:",len(fruta)) #função len, retorna o tamanho