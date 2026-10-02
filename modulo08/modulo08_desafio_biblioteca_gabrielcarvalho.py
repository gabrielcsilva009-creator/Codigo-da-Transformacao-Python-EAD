class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_info(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"

    def __str__(self):
        return f"{self.titulo} - {self.autor}"


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def exibir_livros(self):
        if not self.livros:
            print("A biblioteca está vazia.")
        else:
            print("Livros disponíveis:")

            for livro in self.livros:
                print(livro)


livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("O Cortiço", "Aluísio Azevedo")
livro3 = Livro("Harry Potter", "J. K. Rowling")

biblioteca = Biblioteca()

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

biblioteca.exibir_livros()