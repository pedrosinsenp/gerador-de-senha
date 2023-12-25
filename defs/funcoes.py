from time import sleep

def verificar_num(msg, num=0, senha=False):
    """
    \033[3;93m-> Essa função serve para garantir que o programa não de erro por conta de digitação.

    \033[93mArgs:
        \033[94m- msg (str):\033[m Mensagem que aparecerá ao usuario.
        \033[94m- num (int, optional):\033[m Deve ser colocado quando existir um limite de número máximo. Defaults to 0.

    \033[93mReturns:
        \033[94m- resultado:\033[m Irá retornar o resultado que o usuario digitar
    """
    
    while True:
        try:
            a = str(input(f'{msg}\033[92m')).strip().replace(',', '.')
            a = int(a)

            if senha == True:
                if a < 8:
                    print(f'\033[91mPara sua segurança, escolha uma senha com 8 ou mais caracteres.\033[m')
                    continue
            elif num == 0:
                if a == 0:
                    print(f'\033[91mERRO! \033[3mDigite um número maior que 0\033[m')
                    continue
            else:
                if a > num:
                    print(f'\033[91mERRO! \033[3mDigite um número menor que {num + 1}\033[m')
                    continue
                elif a == 0:
                    print(f'\033[91mERRO! \033[3mDigite um número maior que 0\033[m')
                    continue
        except (TypeError, ValueError):
            if '.' in a:
                print(f'\033[91mERRO! \033[3mDigite um valor inteiro.\033[m')
                continue
            else:
                print(f'\033[91mERRO! \033[3m"{a}" não é válido.\033[m')
                continue
        except KeyboardInterrupt:
            print('\033[3;91mO usuário preferiu finalizar o programa.\033[m')
            sleep(0.8)
            exit()
        else:
            return a
        
def continuar_def(msg='<desconhecido>', pular=False):
    """
    \033[3;93m-> Pergunta ao usuario se deseja continuar.

    \033[93mArgs:
        \033[94m- msg (str):\033[m Mensagem que aparecerá na pergunta. Defaults to '<desconhecido>'.
        \033[94m- pular (bool, optional):\033[m Se verdadeira, irá dar quebra de linha. Defaults to False.
    """
    
    global continuar
    while True:
        try:
            if pular == False:
                continuar = str(input(f'{msg}? [S/N]\033[92m ')).upper().strip()[0]
            else:
                continuar = str(input(f'\n{msg}? [S/N]\033[92m ')).upper().strip()[0]
            
            if continuar != 'S' and continuar != 'N':
                print(f'\033[91mERRO! \033[3m"{continuar}" não é válido.\033[m')
                continue
        except KeyboardInterrupt:
            print('\033[3;91mO usuário preferiu finalizar o programa.\033[m')
            sleep(0.8)
            exit()
        else:
            return continuar
        

def finalizar():
    print('\033[m\033[3mSaindo do gerador de senha...\033[m')
    linha()
    sleep(0.8)


def linha():
    print('\033[94m~\033[m'*60)


def titulo():
    linha()
    print(f'\033[3m{("GERADOR DE SENHAS"):^60}\033[m')
    linha()


def menu(*n):
    for i, c in enumerate(n):
        print(f'\033[94m{f"[ {i + 1} ]":>9}\033[m - \033[3m{c}\033[m')