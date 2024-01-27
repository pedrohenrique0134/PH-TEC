# a = 1
# def teste():
#     a = 2
#     print(a)

# teste()
# print(a)


# num = float(input("digite um numero fracional: "))

# def conv_int(num):
#     return int(num)

# print(conv_int(num))


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# def soma(a,b,c,d):
#     return a+b+c+d

# print(soma(a,b,c,d))

# print('ola mundo')

# print('ola', 'mundo','pedroca',sep='...',end=' ')

# print('casa')

# a = '1'
# b = 'henrique'

# def funcao(a,b="default"):
#     return f'{a} {b}'

# print(funcao(2,1))


# def imprima(a="default"):
#     return f'{a}'

# print(imprima(2))



## faca uma função que receba uma inteio e imprime se este valor é par ou impar?

# numero_qualquer = float(input("digite um numero qualquer: "))

# def indentificador(valor):
#     return valor % 2 == 0

# print(indentificador(numero_qualquer))

remover_vogais = input('')

def remover_vogais(frase):
    vogais = "aeiouAEIOU"
    resultado = [letra for letra in frase if letra not in vogais]
    return resultado

        