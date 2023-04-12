def desiçao(p1,p2):
    if p1=='TESOURA':
        if p2=="TESOURA":
            print('EMPATE')
        elif p2=="PEDRA":
            print('p1 ganhou')
        elif p2=="PAPEL":
            print('p2 ganhou')
    elif p1=="PEDRA":
        if p2=="TESOURA":
            print('p1 ganhou')
        elif p2=="PEDRA":
            print('EMPATE')
        elif p2=="PAPEL":
            print('p2 ganhou')
    elif p1=="PAPEL":
        if p2=="TESOURA":
            print('p2 ganhou')
        elif p2=="PEDRA":
            print('p1 ganhou')
        elif p2=="PAPEL":
            print('EMPATE')

while True:
    while True:
        try:
            pl1=input(str("digite o tesoura,pedra,papel p/p1 "))
            pl2=input(str("digite o tesoura,pedra,papel p/p2 "))
        except ValueError:
            print("digitou algo indevido , digite novamente:")
        p1=pl1.upper()
        p2=pl2.upper()
        desiçao(p1,p2)
        xL=input("deseja continrua?s/n ")
        x=xL.upper()
        if x == 'N':
            break
