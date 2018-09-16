# -*- coding: utf-8 -*-

import sys

def tabela(chave, alfabeto):
    i = 0
    matriz=[["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
    for x in range(0,5):
        for y in range(0,5):
            if(i!=len(chave)):
                matriz[x][y]=chave[i]
                alfabeto.remove(chave[i])
                i=i+1
            else:
                matriz[x][y]=alfabeto[0]
                del alfabeto[0]
    return matriz 


def criptografia(matriz,matrizT,mensagem):  
    pares=[]
    if (len(mensagem)%2 != 0):
            mensagem += "x"
    looping = len(mensagem)
    for x in range(0,looping,2):
        pares.append(mensagem[x:x+2])
    tamanho = len(pares)
    #ta certo até aqui.
    for y in range(0,tamanho):
        for y1 in range(0,5):
            if(pares[y][0] in matriz[y1] and  pares[y][1] in matriz[y1]):
                a = matriz[y1].index(pares[y][0])+1
                b = matriz[y1].index(pares[y][1])+1
                if(b>4):
                    b=b-4
                if(a>4):
                    a=a-4
                pares[y]=matriz[y1][a]+matriz[y1][b]
                #terminado sobre a mesma linha
            if((pares[y][0] in matrizT[y1]) and  (pares[y][1] in matrizT[y1])):
                a = matrizT[y1].index(pares[y][0])+1
                b = matrizT[y1].index(pares[y][1])+1
                if(b>4):
                    b=0
                if(a>4):
                    a=0 
                pares[y]=matrizT[y1][a]+matrizT[y1][b]
                #terminado sobre a mesma coluna 
        else:
            linha2=0
            coluna2=0
            linha1=0
            coluna1=0
            for x1 in range(0,5):
                for x2 in range(0,5):
                    if(pares[y][0]== matriz[x1][x2]):
                        coluna1 = int(x1)
                        linha1 = int(x2)
                    if(pares[y][1]== matriz[x1][x2]):
                        coluna2 = int(x1)
                        linha2 = int(x2)
            pares[y] = matriz[coluna1][linha2]+matriz[coluna2][linha1]
    mensagemclara=[]                 
    for f in range(0,tamanho):
        mensagemclara.append(pares[f])  
    mensagemclara = ''.join(mensagemclara)     
    print(mensagemclara)
    return 0 



def descriptografar(matriz,matrizT,mensagem):  
    pares=[]
    if (len(mensagem)%2 != 0):
            mensagem += "x"
    looping = len(mensagem)
    for x in range(0,looping,2):
        pares.append(mensagem[x:x+2])
    tamanho = len(pares)
    #ta certo até aqui.
    for y in range(0,tamanho):
        for y1 in range(0,5):
            if(pares[y][0] in matriz[y1] and  pares[y][1] in matriz[y1]):
                a = matriz[y1].index(pares[y][1])-1
                b = matriz[y1].index(pares[y][0])-1
                if(b>4):
                    b=b-4
                if(a>4):
                    a=a-4
                pares[y]=matriz[y1][a]+matriz[y1][b]
                #terminado sobre a mesma linha
            if((pares[y][1] in matrizT[y1]) and  (pares[y][0] in matrizT[y1])):
                a = matrizT[y1].index(pares[y][0])-1
                b = matrizT[y1].index(pares[y][1])-1
                if(b>4):
                    b=0
                if(a>4):
                    a=0 
                pares[y]=matrizT[y1][a]+matrizT[y1][b]
                #terminado sobre a mesma coluna 
        else:
            linha2=0
            coluna2=0
            linha1=0
            coluna1=0
            for x1 in range(0,5):
                for x2 in range(0,5):
                    if(pares[y][0]== matriz[x1][x2]):
                        coluna1 = int(x1)
                        linha1 = int(x2)
                    if(pares[y][1]== matriz[x1][x2]):
                        coluna2 = int(x1)
                        linha2 = int(x2)
            pares[y] = matriz[coluna1][linha2]+matriz[coluna2][linha1]
    mensagemclara = []                 
    for f in range(0,tamanho):
        mensagemclara.append(pares[f])  
    mensagemclara = ''.join(mensagemclara)     
    print(mensagemclara)

alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","z"]
nome_path =''
print("\nBem vindo ao programa de criptografia do Pascal !! hihi \n")
print("*******************************************************\n")
escolha = input("Digite número 1 para criptografar.\nDigite número 2 para descriptografar\n")
if (int(escolha) == 1 ):
    print("\n*******************Criptografia**********************\n")
    nome_path = input("Digite o nome ou path do arquivo para ser cifrado: \n")
    try:
        arq = open (nome_path , 'r')
        path = arq.read()
        arq.close()
        path = path.lower()
    except:
        print("Patch não encontrado\n*********Bye Bye***********\n")
        sys.exit() 
    chave = input("Digite a chave: ")
    chave = chave.lower()
    chave = chave.replace(" ", "")
    matriz = tabela(chave,alfabeto)
    matrizT=[["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
    for x in range(0,5):
        for y in range(0,5):
            matrizT[x][y]= matriz[y][x]
    a =criptografia(matriz,matrizT,path)

elif(int(escolha)==2):
    print("\n*******************Descriptografia**********************\n")
    nome_path = input("Digite o nome ou path do arquivo para ser cifrado: \n")
    try:
        arq = open (nome_path , 'r')
        path = arq.read()
        arq.close()
        path = path.lower()
    except:
        print("Patch não encontrado\n*********Bye Bye***********\n")
        sys.exit() 
    chave = input("Digite a chave: ")
    chave = chave.lower()
    chave = chave.replace(" ", "")
    matriz = tabela(chave,alfabeto)
    matrizT=[["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
    for x in range(0,5):
        for y in range(0,5):
            matrizT[x][y]= matriz[y][x]
            
    print("Valor descriptografado com o X em valores repetidos :)")
    descriptografar(matriz,matrizT,path)


#Tratar os repetidos na chave.