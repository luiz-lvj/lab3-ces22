from abc import ABC, abstractmethod

class Bolo(ABC):
    def __init__(self, estilo, cobertura):
        self.estilo = estilo
        self.cobertura = cobertura
        self.tipo = self._prepare_type()

    @abstractmethod
    def _prepare_type(self):
        raise NotImplementedError("É necessário implementar!")
    
    def show_cake(self):
        str_tipo = "Tipo: " + self.tipo + "\n"
        str_estilo = "Estilo: " + self.estilo + "\n"
        str_cobertura = "Cobertura: " + self.cobertura + "\n\n"
        str_cake = str_tipo + str_estilo + str_cobertura
        print(str_cake)
        return str_cake

class BoloDeChocolate(Bolo):
    def _prepare_type(self):
        return "Bolo de Cenoura"

class BoloDeCenoura(Bolo):
    def _prepare_type(self):
        return "Bolo de Chocolate"

class BoloDeMandioca(Bolo):
    def _prepare_type(self):
        return "Bolo de Mandioca"

class BoloQualquer(Bolo):
    def _prepare_type(self):
        return "Bolo qualquer"

# --------------------- TESTES ----------------------

bolo1 = BoloDeCenoura("casamento", "chocolate")
bolo2 = BoloDeChocolate("festa", "morango")
bolo3 = BoloDeMandioca("tradicional","abacaxi")
bolo4 = BoloQualquer("casamento", "azul")

bolos = [bolo1, bolo2, bolo3, bolo4]

for bolo in bolos:
    bolo.show_cake()




