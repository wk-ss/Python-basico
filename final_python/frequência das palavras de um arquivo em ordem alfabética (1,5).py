while True:
        nome = (input("Digite o nome do arquivo : "))
        try:
            with open(f'{nome}.txt', 'r') as arquivo:
                conteudo = arquivo.read()
                print(conteudo)
                palavras = conteudo.split()
                frequencias = {}
                for palavra in palavras:
                    if palavra in frequencias:
                        frequencias[palavra] += 1
                    else:
                        frequencias[palavra] = 1
            for palavra, frequencia in sorted(frequencias.items()):
                print(palavra, ":", frequencia)
                
        except:
            print("nome nao encontrado digite o nome do arquivo ")