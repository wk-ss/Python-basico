d=[]
with open('k.txt', 'r') as lendo:
    arquivo=lendo.readlines()
    ar=lendo.read()
    ab=lendo.readline()
    print("1-----")
    print(arquivo)
    print("2-----")   
    print(ar)
    print("3-----")
    print(ab)
    print("1-----")
    for c in arquivo:
        print (c)
        d.append(c)
        for k in d:
            print(k)
    print("1-----")
    print(d)