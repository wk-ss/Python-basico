a=[1,2,3,4,5,]
b=[8,1,9,2]
def ElementoEmComn(a,b):
    c=[]
    for i in range(len(a)):
      for o in range(len(b)):   
        if a[i]== b[o] and a[i] not in c:
            c.append(a[i])
    return c
        
casa=ElementoEmComn(a,b)
print(casa)