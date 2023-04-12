class Endereco:
    def __init__(self, rua, num, bairro, cidade, cep):
        self.nome_rua = rua
        self.numero = num
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep

class EnderecoCin(Endereco):
    def __init__(self, sala,rua="Av. Jornalista Anibal Fernandes", num="s/n", bairro="Cidade Universitária (Campus Recife)", cidade="Recife", cep="50740-560"):
        super().__init__(rua, num, bairro, cidade, cep)
        self.sala=sala

aline=EnderecoCin('21','Agamenon')
print(aline.sala)
print(aline.cep)
print(aline.bairro)
print(aline.cidade)
print(aline.numero)