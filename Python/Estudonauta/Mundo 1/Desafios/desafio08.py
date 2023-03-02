metros = float(input('Digite a medida em metros: '))

cm = metros * 100
mm = metros * 1000
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10

print(f'A medida em Kilometros é {km}')
print(f'A medida em hectometro é {hm}')
print(f'A medida em decametro é {dam}')
print(f'A medida em decimetro é {dm}')
print(f'A medida em centrimetros é {cm}')
print(f'E em milimetros é {mm}')
