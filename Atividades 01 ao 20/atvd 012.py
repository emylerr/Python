'''dobro, triplo e raiz'''
n1 = int(input('digite 01 número: '))
r_f = '{:.1f}'.format(n1**(1/2))
print(f'o dobro do seu número é de {n1*2} o triplo é {n1*3}', end=', ')
print(f'a raiz quadrada é {r_f}')