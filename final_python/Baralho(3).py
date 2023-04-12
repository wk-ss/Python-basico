import random

class Carta:
    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor
    
    def __repr__(self):
        return "{} de {}".format(self.valor, self.naipe)

class Baralho:
    naipes = ['COPAS', 'OUROS', 'PAUS', 'ESPADAS']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    
    def __init__(self):
        self.cartas = []
        for naipe in self.naipes:
            for valor in self.valores:
                self.cartas.append(Carta(naipe, valor))
                
    def embaralhar(self):
        if not self.cartas:
            raise ValueError("Baralho vazio")
        random.shuffle(self.cartas)
        
    def puxar(self):
        if not self.cartas:
            raise ValueError("Baralho vazio")
        return self.cartas.pop()

deck = Baralho()
while True:
    decisao= int(input("Digite uma das opçoes abaixo:\n"+'1)embaralhar o deck:\n2)Puxar carta:'))
    if decisao==1:
        deck.embaralhar()
    elif decisao==2:
        quantidade=int(input("Digite a quantidade de carta que deseja sacar:"))
        for c in range (quantidade):
            print(deck.puxar())
    else:
        print("VC digitou algum numero nao aceito,digite novamente")

