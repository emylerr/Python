'''altura x largura'''
larg = float(input('digite a largura da sua parede em metros: '))
alt = float(input('digite altura da sua parede em metros: '))
tint = 2 ** 2/1
a = alt * larg
res = a * 2 / tint
print(f'a área é de {a} e você precisará de {res} latas de tinta!')