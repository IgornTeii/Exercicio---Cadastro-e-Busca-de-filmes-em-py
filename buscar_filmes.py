import csv

def exibir_por_titulo():
    titulo_desejado = input("Digite o título do filme que você está procurando: ")
    with open('filmes.csv', 'r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)
        encontrou = False
        for linha in leitor:
            if titulo_desejado.lower() in linha[0].lower():
                print(f"Título: {linha[0]}, Gênero: {linha[1]}, Duração: {linha[2]}, Censura: {linha[3]}, Diretor: {linha[4]}")
                encontrou = True
        if not encontrou:
            print("Título não encontrado.")

def exibir_por_diretor():
    diretor_desejado = input("Digite o nome do diretor que você está procurando: ")
    with open('filmes.csv', 'r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)
        encontrou = False
        for linha in leitor:
            if diretor_desejado.lower() in linha[4].lower():
                print(f"Título: {linha[0]}")
                encontrou = True
        if not encontrou:
            print("Nenhum filme encontrado para esse diretor.")

def exibir_por_genero():
    genero_desejado = input("Digite o gênero de filme que você está procurando: ")
    with open('filmes.csv', 'r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)
        encontrou = False
        for linha in leitor:
            if genero_desejado.lower() in linha[1].lower():
                print(f"Título: {linha[0]}")
                encontrou = True
        if not encontrou:
            print("Nenhum filme encontrado para esse gênero.")

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Buscar por título")
        print("2. Buscar por diretor")
        print("3. Buscar por gênero")
        print("4. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            exibir_por_titulo()
        elif escolha == "2":
            exibir_por_diretor()
        elif escolha == "3":
            exibir_por_genero()
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
