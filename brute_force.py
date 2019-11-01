# -*- coding: UTF-8 -*-
'''
Autor: Carlos Adolfo Guedes Gondim
Descricao: Codigo de brute-force simples, desenvolvido para 
apresentacao sobre Criptografia, na disciplina de 
REDES 2 ministrada pela profa Atslands para
alunos de Engenharia de Computacao da Universidade Federal do Ceara

Apenas caracteres ASCII, nao UTF-8
'''
import random

def titulos():
	titulos = ['jovem', 'ser humano', 'Bob Esponja', 'Cyndy Lauper', 'Lois Lane', 'Bob Dylan', 'André Matos', 'Kate Pierson', 'Cazalbé de Nóbrega da Praça é Nossa', 'Dona Florinda', 'Professor Linguiça', 'Elo Perdido', 'Buchudim', 'meu Pleonasmo Vicioso']
	return random.choice(titulos)

def msg_erro():
	msgs_erro = ['Vou fingir que nem vi', 'Vá estudar', 'Por favor, só me chame se for coisa séria', 'Dá proxima vez eu me formato pra te deixar na merda', 'Eu queria ser formatado pra você não fazer mais essas coisas comigo', 'Queria ser útil, mas você não colabora']
	return random.choice(msgs_erro)

def dados_senha(s):
	print(s + ' - len = '+str(len(s)))

def incrementa_caractere(senha, posicao = 0):
	senha = list(senha)
	if(ord(senha[posicao])+1 < 127): #até 126 que é ~
		senha[posicao] = chr(ord(senha[posicao])+1)
	else: #podemos ter encadeamento
		senha[posicao] = ' '
		if(posicao+1 < len(senha)):
			#se posição+1 é menor que a senha, incrementa o próximo, jovem
			senha = incrementa_caractere(senha, posicao+1)
		else:
			#se já chegamos no fim, basta por um caractere extra
			#inserindo caractere novo, zerado
			senha = senha + [' ']
		
	senha = "".join(senha)
	return senha

def gera_senha(max, min = 1, senha = '' ):
	#se inseriu mínimo, deseja então começar sem senha
	if(min<=0):
		print("Parâmetro de entrada inválido, "+titulos())
		print(msg_erro())
	if(min > 1):
		return (' '*min) #primeira senha. fazer o que?
	#problemas com tamanho de senha mínimo resolvidos
	s = incrementa_caractere(senha)
	return s

s = incrementa_caractere('}~~')
dados_senha(s)
s = incrementa_caractere(s)
dados_senha(s)
s = incrementa_caractere(s)
dados_senha(s)

dados_senha(gera_senha(5,5))