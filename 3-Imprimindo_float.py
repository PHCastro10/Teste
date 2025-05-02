#Qual a media da nota dele:
                      # com o input a entrada sempre sera lida como uma string, ent temos que converter para float
                      # utilizamos map, para converter cada uma das variaves em float
                      # split, separa as strings onde há espaço
nota1, nota2, nota3 = (map (float, input("Digite os valor de nota, cada prova vale 10 pts: ").split()))

                #para escolher quantas casas decimais quer siga o formato:  :.2f
print (f"Nota 1: {nota1:.2f}")
print (f"Nota 2: {nota2:.2f}")
print (f"Nota 3: {nota3:.2f}")
media =  ( (nota1 + nota2 + nota3) / 3)

print (f"Media: {media:.3f}")
print(f"Sua media foi {round(media)}")  #round: arredonda o float para o inteiro mais próximo
