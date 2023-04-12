class Livro:
     def __init__(self, titulo, autor, categoria, isbn):
          self.titulo = titulo
          self.autor = autor
          self.categoria = categoria
          self.isbn = isbn
class Biblioteca(Livro):
    def __init__(self, titulo, autor, categoria, isbn):
        super().__init__(titulo, autor, categoria, isbn)
        self.acervo = {}

    def adicionar_livro(self, quantidade, livro:Livro):
        if livro.isbn in self.acervo:
            self.acervo[livro.isbn][1] += quantidade
        else:
            self.acervo[livro.isbn] = [livro, quantidade]

    def pesquisar_titulo(self, livro:Livro):
    
        for livro.isbn in self.acervo:
            if self.acervo[livro.isbn][0].titulo == livro.titulo:
                return True
        return False

    def pesquisar_autor(self, livro:Livro):
        livros = []
        for livro.isbn in self.acervo:
            if self.acervo[livro.isbn][0].autor == livro.autor:
                livros.append(self.acervo[livro.isbn][0])
        return livros

    def emprestar_livro(self,livro:Livro):
        if livro.isbn not in self.acervo:
            raise IndexError("ISBN não encontrado")
        if self.acervo[livro.isbn][1] > 0:
            self.acervo[livro.isbn][1] -= 1
            return True
        else:
            return False

    def devolver_livro(self, livro:Livro):
        if livro.isbn not in self.acervo:
            raise IndexError("ISBN não encontrado")
        self.acervo[livro.isbn][1] += 1

    def imprimir_livros_por_categoria(self,livro:Livro):
        categorias = {}
        for livro.isbn in self.acervo:
            categoria = self.acervo[livro.isbn][0].categoria=livro.categoria
            if categoria not in categorias:
                categorias[categoria] = []
            categorias[categoria].append(self.acervo[livro.isbn][0])
        for categoria in categorias:
            print(f"Categoria: {categoria}")
            for livro in categorias[categoria]:
                print(f"- {livro.titulo} ({livro.autor})")

    def imprimir_livros_disponiveis(self,livro:Livro):
        print("Livros disponíveis para empréstimo:")
        for livro.isbn in self.acervo:
            if self.acervo[livro.isbn][1] > 0:
                livro = self.acervo[livro.isbn][0]
                print(f"- {livro.titulo} ({livro.autor})")

m1=Livro("princepi","desconhecido",'terror','5679')
bl1=Biblioteca()
bl1.adicionar_livro(2,m1)
m2=("princepi")
bl1.pesquisar_titulo(m2)