from datetime import datetime


class Pessoa:

    anoAtual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar pois está comendo')
            return

        print(f'{self.nome} Esta Falando {assunto}')
        self.falando = True

    def parar_falar(self):
        print(f'{self.nome} não está falando')
        return

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.{alimento}')
            return

        print(f'{self.nome} está comendo.{alimento}')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} Parou de Comer.')
        self.comendo = False

    def GetAnoNascimento(self):
        print(f'{self.nome} nasceu em {self.anoAtual - self.idade}')
        return self.anoAtual - self.idade
