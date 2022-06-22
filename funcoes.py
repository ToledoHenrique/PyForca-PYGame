import os

ciano = '\033[1;36m'
reset = '\033[0;00m'
vermelho = '\033[1;91m'
verde = '\033[1;92m'
magenta = '\033[1;35m'
verdeclaro = '\033[1;32m'


def limpar():
    os.system('cls')


def forcas (erros):
    if erros == 0:
        forca()
    elif erros == 1:
        erro1()
    elif erros == 2:
        erro2()
    elif erros == 3:
        erro3()
    elif erros == 4:
        erro4()
    elif erros == 5:
        erro5()

def historico():
    print(verde + ''' 
    
                                                                 ___
                                                                |   |
                                                                |   |
            .  ___ ___  ____  ____  .  ___  ____              __|   |__
       |__| | |__   |   |  |  |__/  |  |    |  |              \       /
       |  | | ___|  |   |__|  |  \  |  |__  |__|               \     /
                                                                \   /
                                                                 \./

                                                                  ''' + reset )
def competidor():
    print(vermelho + '''
         __ ____ _  _ ____ __ ___  . ___  ____ ____
        |   |  | |\/| |__||__  |   | |  \ |  | |__/
        |__ |__| |  | |   |__  |   | |__/ |__| |  \ 
   __  ____ ____  __   ___   __    ____          ____ ____       
  |__| |__| |__/ |__   |  \ |__    |  | |   |__| |__| |__/       
  |    |  | |  \ |__   |__/ |__    |__| |__ |  | |  | |  \      


    ''' + reset)


def titulo():
    print(verdeclaro + '''
 _ ____ ____ ____    ___  ____    ____ ____ ____ ____ ____ 
 | |  | | __ |  |    |  \ |__|    |___ |  | |__/ |    |__| 
_| |__| |__] |__|    |__/ |  |    |    |__| |  \ |___ |  | 
          \033[1;36m By: Carlos Piva / Henrique Toledo
    ''' + reset)

def forca():
    print('''

    ___________
    |         |
    |
    |
    |
____|____
    ''')

def erro1():
    print('''
    ___________
    |         |
    |        ( )
    |
    |
____|____
        ''')

def erro2():
    print('''

    ___________
    |         |
    |        ( )
    |         |
    |         |
____|____
        ''')

def erro3():
    print('''

    ___________
    |         |
    |        ( )
    |         |\ 
    |         |
____|____
        ''')

def erro4():
    print('''

    ___________
    |         |
    |        ( )
    |        /|\ 
    |         |
____|____
        ''')

def erro5():
    print('''

    ___________
    |         |
    |        ( )
    |        /|\ 
    |         |
____|____      \ 
        ''')

def erro6():
    limpar()
    print('''

    ___________
    |         |
    |        ( )
    |        /|\ 
    |         |
____|____    / \ Você Perdeu! :(
        ''')

def vitoria():
    limpar()
    titulo()
    print('''
    ( ) 
   \ | /
     |
    / \ 
        Você venceu!!!
    ''')

char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
opçoes = ['1','2','3']

    	

