from abc import ABC, abstractmethod


class Director:
    def __init__(self):
        self._builder = None
    
    @property
    def builder(self):
        return self._builder
    
    @builder.setter
    def builder(self, builder):
        self._builder = builder
    
    def build_bolo(self, tipo, estilo, cobertura):
        self.builder.produce_tipo(tipo)
        self.builder.produce_estilo(estilo)
        self.builder.produce_cobertura(cobertura)


class Builder(ABC):

    def __init__(self):
        self._product = Bolo()
    
    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def produce_tipo(self, tipo):
        pass
    
    @abstractmethod
    def produce_estilo(self, estilo):
        pass

    @abstractmethod
    def produce_cobertura(self, cobertura):
        pass


class BoloBuilder(Builder):

    @property
    def product(self):
        product = self._product
        self._product = Bolo()
        return product

    def produce_tipo(self, tipo):
        str_tipo = "Tipo: " + tipo 
        print(str_tipo)
        return tipo

    def produce_estilo(self, estilo):
        str_estilo = "Estilo: " + estilo
        print(str_estilo)
        return estilo

    def produce_cobertura(self, cobertura):
        str_cobertura = "Cobetura: " + cobertura + "\n\n"
        print(str_cobertura)
        return cobertura

class Bolo:
    def __init__(self):
        pass
    

# -------------------- TESTES -----------------------

director = Director()
builder = BoloBuilder()
director.builder = builder

director.build_bolo("Bolo de Chocolate", "casamento", "chocolate")
director.build_bolo("Bolo de Cenoura", "festa", "morango")
director.build_bolo("Bolo de Mandioca", "tradicional", "abacaxi")





    





