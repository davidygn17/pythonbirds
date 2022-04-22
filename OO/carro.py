"""
Voce deve criar uma classe carro que vai possuir dois
atributos compostos por outras duas classes:

1) motor
2)direçao

O motor tera a responsabilidade de controlar a velocidade
ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) metodo acelerar, que devera incrementar a velocidade de uma unidade
3) metodo frear que devera decrementar a velocidade em duas inudades

A direçao tera  a responsablidade de controlar a direçao. Ela oferece os seguintes atributos:
1) valor de direçao com valores possiveis: Norte, Sul, Leste, Oeste.
2) metodo girar_a_direita
3) metodo girar_a_esquerda


    N
  O   L
    S

    Exemplo:
    >>> #testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # testando direçao
    >>> direçao = Direçao()
    >>> direçao.valor
    'norte'
    >>> direçao.girar_a_direita()
    >>> direçao.valor
    'leste'
    >>> direçao.girar_a_direita()
    >>> direçao.valor
    'sul'
    >>> direçao.girar_a_direita()
    >>> direçao.valor
    'oeste'
    >>> direçao.girar_a_direita()
    >>> direçao.valor
    'norte'
    >>> direçao.girar_a_esquerda()
    >>> direçao.valor
    'oeste'
    >>> direçao.girar_a_esquerda()
    >>> direçao.valor
    'sul'
    >>> direçao.girar_a_esquerda()
    >>> direçao.valor
    'leste'
    >>> direçao.girar_a_esquerda()
    >>> direçao.valor
    'norte'
    >>> carro = Carro(direçao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direçao()
    'norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direçao()
    'leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direçao()
    'norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direçao()
    'oeste'



"""
NORTE = 'norte'
SUL = 'sul'
LESTE = 'leste'
OESTE = 'oeste'

class Carro:
    def __init__(self, direçao, motor):
        self.motor = motor
        self.direçao = direçao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direçao(self):
        return self.direçao.valor

    def girar_a_direita(self):
        return self.direçao.girar_a_direita()

    def girar_a_esquerda(self):
        return self.direçao.girar_a_esquerda()


class Direçao:
    rotaçao_a_direita = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }
    rotaçao_a_esquerda = {
        NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL
    }
    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotaçao_a_direita[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotaçao_a_esquerda[self.valor]


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 3
        self.velocidade = max(0, self.velocidade)
