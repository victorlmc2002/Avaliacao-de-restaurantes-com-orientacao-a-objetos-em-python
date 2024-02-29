from modelo.avaliacao import Avaliaco

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):   
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self._nome} | {self._categoria}\n'
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Status".ljust(25)} | {"Avaliação".ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)}')
    @property
    def ativo(self):
        return '✔️' if self._ativo else '❌'
    def alternar_status(self):
        self._ativo = not self._ativo
    def recebe_avaliacao(self, cliente, nota):
        avaliacao = Avaliaco(cliente, nota)
        self._avaliacao.append(avaliacao)
    @property    
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Sem avaliações'
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade = len(self._avaliacao)
        media = round(soma / quantidade, 1)
        return media
    
