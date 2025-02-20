from typing import Dict, Any

livro_01: dict[str, any] = {
    "Titulo": "Diario de um Banana",
    "Autor": "Pedro Damiani",
    "Ano": 2002
}

livro_02: dict[str, any] = {
    "Titulo": "Diario de um Banana 2",
    "Autor": "Pedro Damiani",
    "Ano": 2013
}

lista_de_livros = []

lista_de_livros.append(livro_01)
lista_de_livros.append(livro_02)

lista_dict: dict = {
    "livro 01": {"Titulo": "Diario de um Banana",
    "Autor": "Pedro Damiani",
    "Ano": 2002},

    "livro_02": {"Titulo": "Diario de um Banana 2",
    "Autor": "Pedro Damiani",
    "Ano": 2013}
} 

print(lista_dict["livro_02"])