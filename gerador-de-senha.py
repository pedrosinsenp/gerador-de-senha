from time import sleep
from random import choice
print('\033[94m~\033[m'*60)
print(f'\033[3m{("SEÇÃO DE GERADOR DE SENHAS"):^60}\033[m')
print('\033[94m~\033[m'*60)

while True:
    print('''
    \033[94m[ 1 ]\033[m \033[3mSenha fraca\033[m
    \033[94m[ 2 ]\033[m \033[3mSenha média\033[m
    \033[94m[ 3 ]\033[m \033[3mSenha forte\033[m
    \033[94m[ 4 ]\033[m \033[3mSair\033[m''')
        
    escolha_usuario_gerar_senhas = int(input('\nQual sua opção?\033[92m '))
    while escolha_usuario_gerar_senhas != 1 and escolha_usuario_gerar_senhas != 2 and escolha_usuario_gerar_senhas != 3 and escolha_usuario_gerar_senhas != 4:
        escolha_usuario_gerar_senhas = int(input('\033[91mOpção inválida!\033[m Qual sua opção? \033[1m[1, 2, 3 ou 4]\033[m\033[92m '))

    senha = ''
    if escolha_usuario_gerar_senhas == 1:
        senha_carac = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 'abcdefghijklmnopqrstuvwxyz'
        tamanho_senha = int(input('\033[mQual o tamanho da senha?\033[92m '))
        while tamanho_senha < 8:
            tamanho_senha = int(input('\033[mEscolha uma senha com mais de 8 caracteres:\033[92m '))
        for c in range(0, tamanho_senha):
            escolha = choice(senha_carac)
            senha += escolha
        print(f'\n\033[mA senha gerada foi \033[94m{senha}\033[m')
        escolha_usuario_cont = str(input('Quer gerar mais alguma senha? [S/N]\033[92m ')).upper().strip()[0]
        while escolha_usuario_cont != 'S' and escolha_usuario_cont != 'N':
            escolha_usuario_cont = str(input('\033[91mOpção inválida!\033[m Quer gerar mais alguma senha? \033[1m[S/N]\033[m\033[92m ')).upper().strip()[0]
        if escolha_usuario_cont == 'N':
            print('\033[m\033[3mSaindo do gerador de valores valores\033[m')
            print('\033[94m~\033[m'*60)
            sleep(0.8)
            break

        print('\033[94m~\033[m'*60)
        print('')

    elif escolha_usuario_gerar_senhas == 2:
        senha_carac = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 'abcdefghijklmnopqrstuvwxyz' + '1234567890'
        tamanho_senha = int(input('\033[mQual o tamanho da senha?\033[92m '))
        while tamanho_senha < 8: 
            tamanho_senha = int(input('\033[mEscolha uma senha com mais de 8 caracteres:\033[92m '))
        for c in range(0, tamanho_senha):
            escolha = choice(senha_carac)
            senha += escolha
        print(f'\n\033[mA senha gerada foi \033[94m{senha}\033[m')
        escolha_usuario_cont = str(input('Quer gerar mais alguma senha? [S/N]\033[92m ')).upper().strip()[0]
        while escolha_usuario_cont != 'S' and escolha_usuario_cont != 'N':
            escolha_usuario_cont = str(input('\033[91mOpção inválida!\033[m Quer gerar mais alguma senha? \033[1m[S/N]\033[m\033[92m ')).upper().strip()[0]
        if escolha_usuario_cont == 'N':
            print('\033[m\033[3mSaindo do gerador de valores valores\033[m')
            print('\033[94m~\033[m'*60)
            sleep(0.8)
            break

        print('\033[94m~\033[m'*50)
        print('')
    
    elif escolha_usuario_gerar_senhas == 3:
        senha_carac = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 'abcdefghijklmnopqrstuvwxyz' + '1234567890' + '!#$%&*/?@\_'
        tamanho_senha = int(input('\033[mQual o tamanho da senha?\033[92m '))
        while tamanho_senha < 8:
            tamanho_senha = int(input('\033[mEscolha uma senha com mais de 8 caracteres:\033[92m '))
        for c in range(0, tamanho_senha):
            escolha = choice(senha_carac)
            senha += escolha
        print(f'\n\033[mA senha gerada foi \033[94m{senha}\033[m')
        escolha_usuario_cont = str(input('Quer gerar mais alguma senha? [S/N]\033[92m ')).upper().strip()[0]
        while escolha_usuario_cont != 'S' and escolha_usuario_cont != 'N':
            escolha_usuario_cont = str(input('\033[91mOpção inválida!\033[m Quer gerar mais alguma senha? \033[1m[S/N]\033[m\033[92m ')).upper().strip()[0]
        if escolha_usuario_cont == 'N':
            print('\033[m\033[3mSaindo do gerador de senhas\033[m')
            print('\033[94m~\033[m'*60)
            sleep(0.8)
            break

        print('\033[94m~\033[m'*60)
        print('')
    
    else:
        print('\033[m\033[3mSaindo do gerador de senhas\033[m')
        print('\033[94m~\033[m'*60)
        sleep(0.8)
        break

print('\033[3;93mPrograma finalizado. Volte Sempre!\033[m')