#Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
#A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

#Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.


print('Qual seu nome: ')
nome = input()

executar = True

while executar == True:

    print('Qual ano você nasceu? ')

    try:
        ano = int(input())
        
        if ano < 1922 or ano > 2021:

            print('O ano tem que ser entre 1922 e 2021!')

        else:

            idade = 2023 - ano

            print('Você', nome, 'fez ou ira fazer', idade, 'anos de idade em 2023')

            executar = False
        
    except:

        print('Digite apenas numero em sua idade')