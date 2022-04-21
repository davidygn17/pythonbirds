class Pessoa:
    olhos = 2
    def __init__(self, *filhos,  nome=None, idade=29 ):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola Mundo {id(self)}'

    @staticmethod
    def metedo_estatico():
        return 30

    @classmethod
    def nome_e_atributos_de_classes(cls):
        return f'{cls} - olhos {cls.olhos}'


if __name__ == '__main__':
    david = Pessoa(nome='david')
    luciano = Pessoa(david, nome='Luciano')
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
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(david.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(david.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classes(), luciano.nome_e_atributos_de_classes())
