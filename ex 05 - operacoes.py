'''n1 = int(input('um valor: '))
n2 = int(input('segundo valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma é {} \n o produto é {} \n a divisão é {:.3f}'.format(s, m, d), end='\n ')
print('a divisão inteira é {} \n e potência é {}'.format(d, e))'''

'''desafio da aula - 01'''
n1 = int(input('digite seu número: '))
print('seu antecessor é {} e seu sucessor é {}'.format(n1-1, n1+1))

'''desafio da aula - 02'''
n1 = int(input('digite seu 1° número: '))
print('o dobro do seu número é de {} o triplo é {}'.format (n1*2, n1*3), end=', ')
print('a raiz qaudrada é {}'.format(n1**(1/2)))

'''desafio da aula - 03'''
n1 = float(input('digite sua 1ª nota: '))
n2 = float(input('digite sua 2ª nota: '))

media = (n1 + n2) / 2
media_f = '{:.1f}'.format(media)

print('a média da suas notas foram: {}'.format(media_f))

'''desafio da aula - 04'''
n1 = int(input('digite um número da tabuada: '))
res = n1 * 1
print('a tabuada desse número é: \n')
print('{} x 1 = {}'.format(n1, res))
print('{} x 2 = {}'.format(n1, res*2))
print('{} x 3 = {}'.format(n1, res*3))
print('{} x 4 = {}'.format(n1, res*4))
print('{} x 5 = {}'.format(n1, res*5))
print('{} x 6 = {}'.format(n1, res*6))
print('{} x 7 = {}'.format(n1, res*7))
print('{} x 8 = {}'.format(n1, res*8))
print('{} x 9 = {}'.format(n1, res*9))
print('{} x 10 = {}'.format(n1, res*10))

'''desafio da aula - 05'''
d = float(input('qual é o valor atual da sua carteira(em reais)? '))
dol = d / 3.27
dol_f = '{:.3f}'.format(dol)
print('você pode comprar {} dólares!'.format(dol_f))

'''desafio da aula - 06'''
larg = float(input('digite a largura da sua parede em metros: '))
alt = float(input('digite altura da sua parede em metros: '))
tint = 2 ** 2/1
a = alt * larg
res = a * 2 / tint
print('a área é de: {}, e você precisará de {} latas de tinta!'.format(a, res))