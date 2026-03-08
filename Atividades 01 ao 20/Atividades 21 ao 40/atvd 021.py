'''aluguel de carros'''
alug = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km rodados? '))
res = alug * 60 + 0.15 * km
print(f'O total a pagar é de R${res:.2f}')