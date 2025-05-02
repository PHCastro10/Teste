#Python has two primitive loop commands:
# .while .for

"""i = 0
while i < 5:
    print(i)
    i += 1"""

for x in range(5,0,-1):  #o terceiro é quanto ira acrecentar ou descrencentar 
    print(x)

nome = "Pedro"
for x in nome:
    print(x, end=" ") # usa um espaço em vez de soltar as linhas
    
print(nome[0])