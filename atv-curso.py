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