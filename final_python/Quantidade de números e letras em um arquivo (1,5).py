palavras = []
while True:
        nome = (input("digite o nome do arquivo : "))
        try:
            with open(f"{nome}.txt","r") as tesxto:
                frases=tesxto.readlines()
                for c  in frases:
                    palavras.append(c)
                    n_digitos = sum(1 for caractere in c if caractere.isdigit())
                    n_letras = sum(1 for caractere in c if caractere.isalpha())
                    n_maiusculas = sum(1 for caractere in c if caractere.isupper())
                    n_minusculas = sum(1 for caractere in c if caractere.islower())
                    print(f" Total de dígitos: {n_digitos}")
                    print(f" Total de letras: {n_letras}")
                    print(f" Total de letras maiúsculas: {n_maiusculas}")
                    print(f" Total de letras minúsculas: {n_minusculas}")
                    print("-=-"*5)
        except:
            print("nome nao encontrado digite o nome do arquivo ")


