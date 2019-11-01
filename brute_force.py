# -*- coding: UTF-8 -*-
'''
Autor: Carlos Adolfo Guedes Gondim
Descricao: Codigo de brute-force simples, desenvolvido para 
apresentacao sobre Criptografia, na disciplina de 
REDES 2 ministrada pela profa Atslands para
alunos de Engenharia de Computacao da Universidade Federal do Ceara

Apenas caracteres ASCII, nao UTF-8
'''

def gera_senha(min, max, ultima_senha):
	

def incrementa_caractere(senha, posicao):
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

s = incrementa_caractere('}~~', 0)
print(s + ' - len = '+str(len(s)))
s = incrementa_caractere(s, 0)
print(s + ' - len = '+str(len(s)))
s = incrementa_caractere(s, 0)
print(s + ' - len = '+str(len(s)))