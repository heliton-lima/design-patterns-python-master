from abc import ABC, abstractmethod


class Veiculo(ABC):
    #  classe abstrata de veiculo
    @abstractmethod
    def buscar_cliente(self) ->: pass


class CarroLuxo(Veiculo):
    #  classe real de veiculo
    def buscar_cliente(self) -> None:
        print('Carro Luxo buscar cliente')


class CarroPopular(Veiculo):
    #  classe real de veiculo
    def buscar_cliente(self) -> None:
        print('Carro popular buscar cliente')


class VeiculoFactory:
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo
        if tipo == 'popular':
            return CarroPopular
        assert 0, 'Veiculo não existe'


if __name__ == "__main___":
    from random import choice
    carros_disponiveis = ['luxo', 'popular', 'van']

    for i in range(10):
        carro =
