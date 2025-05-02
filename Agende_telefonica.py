import os #importando biblioteca para limpar o terminal 
agenda_telefonica = {
    'Pedro': {
        "número": 34999828322
    },
    "Luan" : {
        "número": 34999867778
    },
    "Pereira" : {
        "número": 36999854593
    },
    "Sara" : {
        "número": 34974647474
    }
}
while True:
    os.system("cls")  #limpar tela do terminal
    print("Opções:")
    print("Digite 1: ver todos contatos")
    print("Digite 2: Buscar contato")
    print("Digite 3: Mudar número de contato")
    print("Digite 4: Adicionar contato")
    print("Digite 5: Remover contato")
    print("Digite 0: Sair")
    print("------------"*7)
    ação = int(input("Digite um número: "))
    if ação == 0: break
    elif ((ação > 5) & (ação < 1)):print("Essa opção não existe.")
    else:
        #1-Imprimindo todos contatos e respectivos números
        if ação == 1:
            for nome1, rest1 in agenda_telefonica.items():
                print("Nome:",nome1)
                for x1 in rest1:
                    print("Número:", agenda_telefonica[nome1][x1])
            vazio = input("Aperte qualquer tecla para voltar ao menu: ")
        #2- Buscando um contato           
        elif ação == 2:
            nome2 = input("Digite o contato: ")
            if nome2 in agenda_telefonica:
                    for x2 in agenda_telefonica[nome2].values():
                        numero2 = x2
                    print(f"Contato: {nome2}\nNúmero:{numero2}")
            
            else: print("Esse contato não existe!")
            print("-----"*4)
            vazio = input("Aperte qualquer tecla para voltar ao menu: ")
        #3- Mudando número de contato
        elif ação == 3:
            contato3 = input("Digite o contato que queira mudar: ") #vendo qual o contato
            if contato3 in agenda_telefonica:
                print("-----"*4)
                #imprimindo o contato e respectivo número
                numero3 = 0
                for x3 in agenda_telefonica[contato3].values():
                    numero3 = x3
                    print(f"Contato:{contato3}\nNúmero:{numero3}")
                print("-----"*4)
                #recebendo o novo número 
                new_number = int(input("Digite um novo número: "))
                #vendo se realmente que fazer a ação 
                print(f"Gostaria mudar o numero de {contato3} para {new_number}?")
                print("-----"*6)
                confirmação = int(input("Se sim digite: 0\nSe não digete: 1\n"))
                #Mudando o numero
                if confirmação == 0:
                    agenda_telefonica[contato3]["número"] = new_number #mudança de número
                    print("O número foi alterado com sucesso:")
                    print(contato3,"=", agenda_telefonica[contato3])
                    print("-----"*4)
                vazio = input("Aperte qualquer tecla para voltar ao menu: ")
            else: print("Esse contato não existe!!")
            print("-----"*4)
            vazio = input("Aperte qualquer tecla para voltar ao menu: ")
        elif ação == 4:
            #Adicionando um novo contato 
            contato4 = input("Digite o contato que queira adicionar: ")
            new_number4 = int(input(f"Digite o número de {contato4}: "))
            #Salvando na agenda
            ctt = {contato4: {"número": new_number4}} #criando a chave
            agenda_telefonica.update(ctt) #adicionando ao dicionario
            print("Contato adicionado com sucesso!!!")
            print(contato4+"\n",agenda_telefonica[contato4])
            vazio = input("Aperte qualquer tecla para voltar ao menu: ")
            print("-----"*4)
        elif ação == 5: 
            #Removendo contato
            contato5 = input("Digite o contato que queira remover: ")
            agenda_telefonica.pop(contato5) #essa função remove o contato
            print("Contato removido com sucesso")
            print(f"{contato5} não está mais em sua lista telefônica")
            for nome5, rest5 in agenda_telefonica.items():
                print("Nome:",nome5)
                for x5 in rest5:
                    print("Número:", agenda_telefonica[nome5][x5])
            vazio = input("Aperte qualquer tecla para voltar ao menu: ")
            print("-----"*4)





                    