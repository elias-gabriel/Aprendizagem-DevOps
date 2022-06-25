from math import sqrt

opcao = input('Calcular bhaskara? (s/n) ')

if opcao == 'n' or opcao == 'N':
    print('Programa finalizado')
    exit()
elif opcao == 's' or opcao == 'S':
    while opcao == 's' or 'S':
        def raiz_delta():
            a = int(input('Digite o valor de a: '))
            b = int(input('Digite o valor de b: '))
            c = int(input('Digite o valor de c: '))
            delta = (b**2) - (4*a*c)
            raiz_delta = int(sqrt(delta))
            bhaskara1 = (-b + raiz_delta) / (2*a)
            bhaskara2 = (-b - raiz_delta) / (2*a)
            print('\nO delta é: %.2f' %delta)
            print('A raiz é: %.2f' %raiz_delta)
            print('X¹ = %.2f' %bhaskara1)
            print('X² = %.2f' %bhaskara2)
        raiz_delta()
        opcao2 = input('\nDeseja continuar? (s/n) ')
        if opcao2 == 's' or opcao2 == 'S':
            continue
        else:
            print('Programa finalizado, até mais!')
            exit()
else:
    print('Opção inválida')
    exit()