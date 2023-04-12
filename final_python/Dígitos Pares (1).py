def digitosPares(ini, fim):
    n = []
    for n1 in range(ini, fim+1):
        text = str(n1)
        if all(int(numero) % 2 == 0 for numero in text):
            n.append(n1)
    print(n)
ini = int(input("digite um numero: "))
fim = int(input("digite o segundo nummero:"))
digitosPares(ini,fim)
