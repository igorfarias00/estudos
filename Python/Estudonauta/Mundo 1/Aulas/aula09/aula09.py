frase = "Curso em Vídeo Python"

print(f'{frase[9:13]}')

print(f'{frase[9]}')

print(f'{frase[9:21]}')

print(f'{frase[9:21:2]}')

print(f'{frase[:5]}')

print(f'{frase[15:]}') # da posição 15 até o final

print(f'{frase[9::3]}')

print(f'{len(frase)}')

print(f'{frase.count("o")}')

print(f'{frase.count("o",0 ,13)}')

print(f'{frase.find("deo")}')

print(f'{frase.find("android")}')

print(f'{"Curso" in frase}')

print(f'{frase.replace("Python", "android")}')

print(f'{frase}')

print(f'{frase.upper()}')


print(f'{frase.lower()}')


print(f'{frase.capitalize()}')

print(f'{frase.title()}')

frase2 = "   Aprenda Python  "

print(frase2.strip())

print(frase2.rstrip())

print(frase2.lstrip())

print(frase.split())
