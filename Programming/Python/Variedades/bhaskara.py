def bhaskara(a, b, c):
    delta = (b**2) - (4*a*c)
    if delta < 0:
        print('Não existem raízes reais')
    else:
        x1 = (-b + (delta**0.5))/(2*a)
        x2 = (-b - (delta**0.5))/(2*a)
        raiz_del = (delta**0.5)
        print('x1 = {:.2f}'.format(x1))
        print('x2 = {:.2f}'.format(x2))
        print(f'delta = {delta}')
        print(f'raiz delta = {raiz_del}')

if __name__ == '__main__':
    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))
    bhaskara(a, b, c)