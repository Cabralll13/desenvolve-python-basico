import csv
import os

meusLivros = [
    {
        "titulo": "O Caçador de Pipas",
        "autor": "Khaled Hosseini",
        "ano": 2003,
        "paginas": 368
    },
    {
        "titulo": "Torto Arado",
        "autor": "Itamar Vieira Junior",
        "ano": 2019,
        "paginas": 264
    },
    {
        "titulo": "O Senhor dos Anéis",
        "autor": "J.R.R. Tolkien",
        "ano": 1954,
        "paginas": 1200
    },
    {
        "titulo": "1984",
        "autor": "George Orwell",
        "ano": 1949,
        "paginas": 328
    },
    {
        "titulo": "Dom Quixote",
        "autor": "Miguel de Cervantes",
        "ano": 1605,
        "paginas": 1032
    },
    {
        "titulo": "Cem Anos de Solidão",
        "autor": "Gabriel García Márquez",
        "ano": 1967,
        "paginas": 448
    },
    {
        "titulo": "A Revolução dos Bichos",
        "autor": "George Orwell",
        "ano": 1945,
        "paginas": 152
    },
    {
        "titulo": "O Pequeno Príncipe",
        "autor": "Antoine de Saint-Exupéry",
        "ano": 1943,
        "paginas": 96
    },
    {
        "titulo": "Duna",
        "autor": "Frank Herbert",
        "ano": 1965,
        "paginas": 688
    },
    {
        "titulo": "Ensaio sobre a Cegueira",
        "autor": "José Saramago",
        "ano": 1995,
        "paginas": 312
    }
]

arquivo = 'meus_livros.csv'

with open(arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)

    escritor.writerow(
        ["Título", "Autor", "Ano de publicação", "Número de páginas"])

    for livro in meusLivros:
        escritor.writerow([livro["titulo"], livro["autor"],
                          livro["ano"], livro["paginas"]])

caminho = os.path.abspath(arquivo)
print(f"Arquivo '{arquivo}' criado com sucesso!")
print(f"Caminho completo: {caminho}")
print("\nVocê já pode abrir este arquivo com o Excel ou Google Sheets.")
