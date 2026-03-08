'''calculando desconto'''
prod = float(input('digite o preço do seu produto: R$'))
desc = prod * 0.05
res = prod - desc
print(f'o produto que custava {prod}, com 5% de desconto muda para {res:.2f}')