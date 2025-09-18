



#----------------------------------------------------------------------------------------------------------------


# Importazione librerie
import random

class Tartarughe:
    def __init__(self, nome, cappelo, voto):
        self.nome = nome 
        self.cappelo = cappelo
        self.voto = voto
    
    def print_info(self):
        print(f"Nome: {self.nome}, Cappello: {self.cappelo}, Voto: {self.voto}")


jonny = Tartarughe("Jonny", "Rosso", random.randint(1, 10))    
print(jonny.nome)
print(jonny.cappelo)
print(jonny.voto)


micheal = Tartarughe("micheal", "viola", random.randint(1, 10))    
print(micheal.nome)
print(micheal.cappelo)
print(micheal.voto)

#----------------------------------------------------------------------------------------------------------------