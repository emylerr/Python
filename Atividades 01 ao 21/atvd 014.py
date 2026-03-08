'''média de notas'''
n1 = float(input('digite sua 1ª nota: '))
n2 = float(input('digite sua 2ª nota: '))

media = (n1 + n2) / 2
media_f = '{:.1f}'.format(media)

print(f'a média da suas notas foram: {media_f}')