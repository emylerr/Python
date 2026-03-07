val = int (input('digite um valor em metros: '))
km = val / 1000
hm = val / 100
dam = val / 10
dm = val * 10
cm = val * 100
mm = val * 1000
print(f'{val} em metros é igual a {km}km, {hm}hm, {dam}dam, {cm}cm, {dm}dm e {mm}mm.')