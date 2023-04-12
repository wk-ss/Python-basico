import random as r
tentativa=[]
k=r.randrange(1,99)
while True:
    try:
        pl1=int(input("digite o numero entre 1 á 99: ou digite sair para sair do jogo "))
    except:
        pl1=(input("digite novamente sair: "))
    if pl1 == "sair":
        break
    elif pl1>99 or pl1<1:
        print("vc digitou um numero fora do range de 1 ate 99,digite novamente\n\n")
    elif pl1< k  :
        print("o numero digitado foi menor do que numero da sorte,tente novamente\n\n")
        tentativa.append(pl1)
    elif pl1>k :
        print("o numero digitado foi maior do que numero da sorte,tente novamente\n\n")
        tentativa.append(pl1)
    elif pl1== k :
        print(" vc acertou parabes")
        print(f" vc teve {len(tentativa)} e os numeors digitados sao {tentativa}\n\n")
