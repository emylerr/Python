'''tabuada - modelo 01'''
n1 = int(input('um valor: '))
n2 = int(input('segundo valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'a soma é {s} \n o produto é {m} \n a divisão é {d:.3f}', end='\n ')
print(f'a divisão inteira é {di} \n e potência é {e}')
