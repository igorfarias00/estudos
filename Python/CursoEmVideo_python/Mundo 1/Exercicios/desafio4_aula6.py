entrada = input('Digite algo: ')


print('O tipo primitivo dessa variavel é {}'.format(type(entrada)))

print('è um identificador? ', entrada.isidentifier())
print('é da tabelas ascII? ' , entrada.isascii())
print('É letra minuscula? ', entrada.islower())
print('É somente espaços? ', entrada.isspace())
print('É letra maiuscula? ', entrada.isupper())
print('É alfanumerico? ', entrada.isalnum())
print('É numerico? ', entrada.isnumeric())
print('É decimal? ', entrada.isdecimal())
print('É alfabeto? ', entrada.isalpha())
print('É printavel?', entrada.isprintable())
print('É titulo? ', entrada.istitle())
print('É digito? ', entrada.isdigit())