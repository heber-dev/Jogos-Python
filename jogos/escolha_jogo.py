# EsCOLHA O JOGO


import forca
import advinhacao


def escolha_jogo():
    print("*********************************")
    print("********Escolha seu jogo!********")
    print("*********************************")

    print("(1) Forca (2) Advinhação")

    jogo = int(input("Qual o jogo?"))

    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Advinhação!")
        advinhacao.Jogar()

if(__name__ == "__main__"):
    escolha_jogo()