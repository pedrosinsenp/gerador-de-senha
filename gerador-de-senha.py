from time import sleep
from random import choice
from defs import funcoes
from time import sleep
import urllib.request
from webbrowser import open

funcoes.titulo()

while True:
    funcoes.menu('Senha fraca', 'Senha média', 'Senha forte', 'Finalizar programa')
        
    escolha_usuario_gerar_senhas = funcoes.verificar_num('\nQual sua opção?\033[92m ', 4)

    senha = ''
    verificar_especial = verificar_upper = verificar_lower = verificar_num = 0

    let_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    let_lower = 'abcdefghijklmnopqrstuvwxyz'
    num = '1234567890'
    especial = '#$%&?@'
    
    if escolha_usuario_gerar_senhas == 1:
        senha_carac = let_upper + let_lower
        tamanho_senha = funcoes.verificar_num('\033[mQual o tamanho da senha?\033[92m ', senha=True)
        
        while True:
            for c in range(0, tamanho_senha):
                escolha = choice(senha_carac)
                senha += escolha
                if escolha.isupper():
                    verificar_upper = 1
                if escolha.islower():
                    verificar_lower = 1
                    
            if verificar_lower and verificar_upper == 1:
                break
            else:
                senha = ''
                verificar_lower = verificar_upper = 0

        print('\033[3;93mGerando senha...\033[m')
        sleep(0.8)

        print(f'\n\033[mA senha gerada foi \033[94m{senha}\033[m')

        funcoes.continuar_def('Quer gerar mais alguma senha')
        if funcoes.continuar == 'N':
            break
        else:
            funcoes.linha()
            continue

    elif escolha_usuario_gerar_senhas == 2:
        senha_carac = let_upper + let_lower + num
        tamanho_senha = funcoes.verificar_num('\033[mQual o tamanho da senha?\033[92m ', senha=True)

        while True:
            for c in range(0, tamanho_senha):
                escolha = choice(senha_carac)
                senha += escolha
                if escolha.isnumeric():
                    verificar_num = 1
                if escolha.isupper():
                    verificar_upper = 1
                if escolha.islower():
                    verificar_lower = 1

            if verificar_lower and verificar_upper and verificar_num == 1:
                break
            else:
                senha = ''
                verificar_lower = verificar_upper = verificar_num = 0

        print('\033[3;93mGerando senha...\033[m')
        sleep(0.8)

        print(f'\n\033[mA senha gerada foi \033[94m{senha}\033[m')

        funcoes.continuar_def('Quer gerar mais alguma senha')
        if funcoes.continuar == 'N':
            break
        else:
            funcoes.linha()
            continue
    
    elif escolha_usuario_gerar_senhas == 3:
        senha_carac = let_upper + let_lower + num + especial
        tamanho_senha = funcoes.verificar_num('\033[mQual o tamanho da senha?\033[92m ', senha=True)

        while True:
            for c in range(0, tamanho_senha):
                escolha = choice(senha_carac)
                senha += escolha
                if escolha.isnumeric():
                    verificar_num = 1
                if escolha.isupper():
                    verificar_upper = 1
                if escolha.islower():
                    verificar_lower = 1
                if escolha in '!#$&@':
                    verificar_especial = 1
                    
            if verificar_num and verificar_upper and verificar_lower and verificar_especial == 1:
                break
            else:
                senha = ''
                verificar_especial = verificar_lower = verificar_upper = verificar_num = 0

        print('\033[3;93mGerando senha...\033[m')
        sleep(0.8)

        print(f'\n\033[mA senha gerada foi \033[94m{senha}\033[m')

        funcoes.continuar_def('Quer gerar mais alguma senha')
        if funcoes.continuar == 'N':
            break
        else:
            funcoes.linha()
            continue
    
    else:
        break

funcoes.finalizar()

print('\n\033[mObrigado por ultilizar este programa.\033[3;94m Volte Sempre!')
print('https://github.com/pedrosinsenp\033[m')
print('Para contato >> \033[3;94mpedrosinsenp@gmail.com\033[m')

funcoes.tempo()

try:
    urllib.request.urlopen('https://github.com/pedrosinsenp')
except:
    print('Acessa lá meu github!')
else:
    open('https://github.com/pedrosinsenp')