nome=input('Digite seu nome: ')
idade= input('Digite sua idade: ')
print(nome)

with open("base_dados.csv", "a") as arquivo:
    arquivo.write(f'Seja bem vindo(a){nome}.\n')
