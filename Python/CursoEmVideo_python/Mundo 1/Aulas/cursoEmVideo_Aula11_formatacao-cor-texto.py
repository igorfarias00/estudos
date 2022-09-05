# -*- coding: utf-8 -*-
# se precisar de mais opções, pesquisar sobre a biblioteca colorize


#padrao ANSI para cores \033['style'       'texto'      'fundo' m]
#                            0-none         30-padrao   -40
#                            1-BOLD         31 -red     -41
#                            3-Italic                            
#                            4-underline    32 -green   -42
#                            7-negative     33 -yellow  -43
#                                           34 -blue    -44
#                                           35 -violet  -45
#                                           36 -ciano   -46
#                                           37 -gray    -47
                             
# \033[0;33;44m exemplo de codigo
print('\033[0;33;44mOLARR')

#\033[0;30;41m
print('\033[0;30;41m olá')

#\033[4;33;46m
print('\033[4;33;46m olarrrrrrr')


#\033[1;35;43m
print('\033[1;35;43molarrrrrrr')


#\033[30;42m
print('\033[30;42molarrrrrrr')


#\033[m
print('\033[molarrrrrrr')


#\033[7;30m
print('\033[7;30molarrrrrrr')
