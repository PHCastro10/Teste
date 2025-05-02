from random import choice
print("Vamos jogar Pedra, Papel e tesoura")
def jogador():
    esc_jogador = input("Escolha Pedra, Papel ou tesoura: ").lower()
    if esc_jogador in ["pedra","papel","tesoura"]:
        return esc_jogador
    else: 
        print("Essa opção não existe. Tente novamente")
        return jogador()
def resultado(vitoria,empate,derrota):
        print("Vitorias:", vitoria, "Empates:", empate, "Derrotas:", derrota) 

vitoria = 0
derrota = 0
empate = 0
while True:
    esc_maquina = choice(["pedra","papel","tesoura"])
    esc_jogador = jogador()
    print("-----"*8)
    print("O computador escolheu:",esc_maquina)
    print("-----"*8)
    if (esc_jogador == "pedra") and (esc_maquina == "tesoura")\
        or (esc_jogador == "tesoura") and (esc_maquina == "papel")\
        or (esc_jogador == "papel") and (esc_maquina == "pedra"):
        print("Você venceu!!!")
        vitoria = vitoria + 1
        resultado(vitoria,empate,derrota)
    elif esc_jogador == esc_maquina: 
        print ("Deu empate")
        empate += 1
        resultado(vitoria,empate,derrota)
    else: 
        print ("Você perdeu")
        derrota += 1
        resultado(vitoria,empate,derrota)
    jogar_dnv = input("Você gostaria de jogar novamente? ").lower()
    if jogar_dnv in ["s","sim","claro"]:
         print("--------"*8)
         continue
    else:
         print("Obrigado por jogar")
         break



    
