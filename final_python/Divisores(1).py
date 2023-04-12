while True:
    try:
        n=int(input("digite um numero aleatorio:"))
    except:
        n=int(input("vc digitou uma string ,digite um numeoro:"))
    l=[]
    for i in range(1,n+1):
        if (n%i==0):
            l.append(int(n/i))
    print(l)