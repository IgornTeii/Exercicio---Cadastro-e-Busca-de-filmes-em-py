import csv

def cadastrar_filme():
    titulo = input("Digite o título do filme: ")
    genero = input("Digite o gênero do filme: ")
    duracao = input("Digite a duração do filme (em minutos): ")
    censura = input("Digite a censura do filme (em anos): ")
    diretor = input("Digite o diretor do filme: ")
    return [titulo, genero, duracao, censura, diretor]

def salvar_no_csv(filmes):
    with open('filmes.csv', 'w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Título", "Gênero", "Duração", "Ano", "Diretor"])
        escritor.writerows(filmes)

def main():
    filmes = []
    continuar = 's'
    while continuar.lower() == 's':
        filme = cadastrar_filme()
        filmes.append(filme)
        continuar = input("Deseja cadastrar outro filme? (s/n): ")
    salvar_no_csv(filmes)
    print("Filmes salvos com sucesso!")

if __name__ == "__main__":
    main()
