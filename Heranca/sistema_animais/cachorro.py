from animal import Animal

class Cachorro(Animal):
    def emitir_som(self):
        print(f"O cachorro {self.nome} late.")