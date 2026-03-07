'''conversão de reais p/ dolár'''
d = float(input('qual é o valor atual da sua carteira(em reais)? '))
dol = d / 3.27
dol_f = '{:.3f}'.format(dol)
print(f'você pode comprar {dol_f} dólares!')