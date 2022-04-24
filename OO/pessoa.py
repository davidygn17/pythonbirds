class Pessoa:
    olhos = 2
    def __init__(self, *filhos,  nome=None, idade=29 ):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola, meu nome é  {(self.nome)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homen(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return  f'{cumprimentar_da_classe}. Aperto de mao'

class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    david = Mutante(nome='david')
    luciano = Homen(david, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(david.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(david.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(david.olhos))
    pessoa = Pessoa ('Aninomo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homen))
    print(isinstance(david, Pessoa))
    print(isinstance(david, Homen))
    print(david.olhos)
    print(luciano.cumprimentar())
    print(david.cumprimentar())

