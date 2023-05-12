import random

tentativas = 7
num = random.randint(1,100)
print(num)
resposta = int(input("|BEM-VINDO AO JOGO!|\n--Voce tem " + str(tentativas) + " tentativa(s)--\nescolhi um numero de 1 a 100, qual vc acha q é?:\n\n"))

def teste():
    global resposta
    global tentativas
    tentativas = tentativas - 1
    if resposta == num:
        print("\n--VENCEU--\nvc acertou com " + str(tentativas) + " tentativa(s) sobrando! :)")
    elif tentativas > 0:
        if resposta > num:
            resposta = int(input("\n--Você tem " + str(tentativas) + " tentativa(s)--\n" + str(resposta) + " foi alto, o valor é mais baixo :( tente novamente:\n\n"))
            teste()
        if resposta < num:
                resposta = int(input("\n--Você tem " + str(tentativas) + " tentativa(s)--\n" + str(resposta) + " foi baixo, o valor é mais alto :( tente novamente:\n\n")) 
                teste()
    else: 
        print("\n--PERDEU--\nvc perdeu pq acabaram suas tentativas :( ")

teste()