base = int(input("Escreva a largura da parede: "))
altura = int(input("Escreva a altura da parede: "))
area = base * altura

print(f"A area da parede he: {area}")
#vamos considerar que 1l de tinta cobri 10 metros de parede
print(f"Para cobrir os {area}m de parede, gastará {area/10} litros de tinta")