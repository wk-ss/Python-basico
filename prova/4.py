frase = "Esta é uma frase de exemplo."
palavras = [palavra for palavra in frase.split()]
print(palavras)

frase = "Esta é uma frase de exemplo"
lista_palavras = []  # cria uma lista vazia

# Divide a frase em palavras e adiciona cada palavra na lista_palavras
for palavra in frase.split():
    lista_palavras.append(palavra)

print(lista_palavras)
