from time import sleep
from random import choice
from defs import funcoes
from time import sleep

funcoes.titulo()

while True:
    funcoes.menu('Senha fraca', 'Senha média', 'Senha forte', 'Finalizar programa')
        
    escolha_usuario_gerar_senhas = funcoes.verificar_num('\nQual sua opção?\033[92m ', 4)

    senha = ''
    if escolha_usuario_gerar_senhas == 1:
        senha_carac = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 'abcdefghijklmnopqrstuvwxyz'
        tamanho_senha = funcoes.verificar_num('\033[mQual o tamanho da senha?\033[92m ', senha=True)
        
        while True:
            for c in range(0, tamanho_senha):
                escolha = choice(senha_carac)
                senha += escolha
                if escolha.isupper():
                    verificar_maiu = 1
                if escolha.islower():
                    verificar_minu = 1
                    
            if verificar_minu and verificar_maiu == 1:
                break
            else:
                senha = ''
                verificar_minu = 0
                verificar_maiu = 0

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
        senha_carac = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 'abcdefghijklmnopqrstuvwxyz' + '1234567890'
        tamanho_senha = funcoes.verificar_num('\033[mQual o tamanho da senha?\033[92m ', senha=True)

        while True:
            for c in range(0, tamanho_senha):
                escolha = choice(senha_carac)
                senha += escolha
                if escolha.isnumeric():
                    verificar_num = 1
                if escolha.isupper():
                    verificar_maiu = 1
                if escolha.islower():
                    verificar_minu = 1

            if verificar_minu == 1 and verificar_maiu == 1 and verificar_num == 1:
                break
            else:
                senha = ''
                verificar_minu = 0
                verificar_maiu = 0
                verificar_num = 0

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
        senha_carac = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 'abcdefghijklmnopqrstuvwxyz' + '1234567890' + '!#$%&*/?@\_'
        tamanho_senha = funcoes.verificar_num('\033[mQual o tamanho da senha?\033[92m ', senha=True)

        while True:
            for c in range(0, tamanho_senha):
                escolha = choice(senha_carac)
                senha += escolha
                if escolha.isnumeric():
                    verificar_num = 1
                if escolha.isupper():
                    verificar_maiu = 1
                if escolha.islower():
                    verificar_minu = 1
                if escolha in '!#$&@':
                    verificar_carac = 1
                    
            if verificar_minu == 1 and verificar_carac == 1 and verificar_maiu == 1 and verificar_num == 1:
                break
            else:
                senha = ''
                verificar_carac = 0
                verificar_minu = 0
                verificar_maiu = 0
                verificar_num = 0

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

print('\033[3;93mPrograma finalizado. Volte Sempre!\033[m')