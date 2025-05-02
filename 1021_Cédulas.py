#100 50 20 10 5 2
# 1 0.50 0.25 0.10 0.05 0.01
def subitrair(valor_total,troco,qtdd):
       if valor_total >= troco:
            valor_total = round(valor_total,2)
            valor_total =  valor_total - troco
            qtdd = qtdd + 1
            return subitrair(valor_total,troco,qtdd)
       else:
              return qtdd,valor_total
      
      
valor_total = float(input("Digite a quantia em dinheiro: "))
valor_total = round(valor_total,2)
cedulas = (100.00,50.00, 20.00, 10.00,5.00,2.00)
moedas = (1.00, 0.50, 0.25, 0.10, 0.05, 0.01)
qtdd = 0
qtdd_troco = []
qtdd_troco_moedas = []
#qtdd_troco_100 = subitrair(valor_total,troco,qtdd)
for x in cedulas:
    a,b = subitrair(valor_total,x,qtdd)
    qtdd_troco.append(a)
    valor_total = b
for x in moedas:
    a,b = subitrair(valor_total,x,qtdd)
    qtdd_troco_moedas.append(a)
    valor_total = b
print("NOTAS:")
for x in range(len(cedulas)):
      print(f"{qtdd_troco[x]} nota(s) de R$ {cedulas[x]:.2f}")
print("MOEDAS:")
for x in range(len(moedas)):
      print(f"{qtdd_troco_moedas[x]} moeda(s) de R$ {moedas[x]:.2f}")
      
