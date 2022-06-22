from funcoes import *
from time import sleep
import os

reinicio = 'python forca.py'
limpar()

titulo()
Desafiante = input("\nInsira o nome do Desafiante : ")
Competidor = input("\nInsira o nome do Competidor : ")
limpar()

titulo()
competidor()
os.system('pause')
limpar()
titulo()
aletorio = input("Informe Palavra Secreta : ").lower().strip()
palavra = list(aletorio)
dica1 = input("\nDigite a 1° dica : ")
dica2 = input("\nDigite a 2° dica : ")
dica3 = input("\nDigite a 3° dica : ")
limpar()

num = len(palavra)
erros = 0
numletras = []
letras_usadas = []

for c in range(num):
	numletras.append('_')
titulo()
forca()


while True:
	print(f'Letras descobertas : {verde + " ".join(numletras) + reset}')
	print(f'letras erradas : {vermelho + " ".join(letras_usadas) + reset}')
	escolha = int(input("\n(1)Tentar uma letra \n(2)Solicitar Dica\nOpção:"))
	try:
		escolha = int(escolha)
	except:
		print("\nOpção invalida!\n")
		continue
	if escolha == 1:
		letra = input (f'[{magenta}digite uma letra{reset}]-->  ').lower()
	elif escolha == 2:
		dica = int(input(f'[{magenta}digite um numero de para dica{reset}]-->\n[{magenta}(1)1° Dica{reset}]-->\n [{magenta}(2)2° Dica{reset}]-->\n [{magenta}(3)3° Dica{reset}]-->\n'))
		if dica == 1:
			print(f'\n{dica1}\n')
		elif dica == 2:
			print(f'\n{dica2}\n')
		elif dica == 3:
			print(f'\n{dica3}\n')
		else:
			print("\nOpção invalida!\n")
			continue
		letra = input (f'[{magenta}digite uma letra{reset}]-->  ').lower()
	

	limpar()
	titulo()

	if letra not in char or letra in letras_usadas:
		forcas(erros)

	else:
		if letra in palavra:
			for i in range(len(palavra)):
				if palavra[i] == letra:
					numletras.pop(i)
					numletras.insert(i, letra)
			

			forcas(erros)

			if numletras == palavra:
				vitoria()
				print(f'A palavra era { magenta + "".join(palavra)}'+ reset)
				sleep(4)
				open('historico.txt','a').write(f'Ganhador foi Competidor: {Competidor}   |   Perdedor foi Desafiante: {Desafiante}   |   A palavra foi: {aletorio}\n--------------------------------------------------------------------------------------------------------------------\n')
				break

		else:
			erros = erros + 1
			letras_usadas.append(letra)
			forcas(erros)
			if erros == 6:
				erro6()
				print(f'A palavra era {magenta + "".join(palavra)}' + reset)	
				sleep(4)
				open('historico.txt','a').write(f'Perdedor foi Competidor: {Competidor}   |   Ganhador foi Desafiante: {Desafiante}   |   A palavra foi: {aletorio}\n----------------------------------------------------------------------------------------------------------------\n')
				break
		
opção = input("Escolha uma das opçoes\n(1) Jogar Novamente:\n(2) Sair: \n ")
if opção == "1":
	historico()
	print (open('historico.txt','r').read())
	sleep(4)
	os.system(reinicio)
else:
	
	print (magenta + ' > > > > > > > > > > > > > > > > > Obrigado por jogar nossa forca < < < < < < < < < < < < < < < < < ' + reset)
	historico()
	print (open('historico.txt','r').read())
	sleep(4)
	limpar()
