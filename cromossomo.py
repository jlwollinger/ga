from random import randrange
import numpy as np
class Cromossomo:
    genes = []
    aptidao = 0
    
    def acasalar(self, mae):
        filho = CromossomoFactory().build()
        filho.genes = self.genes
        for i in (0, 10): #10 trocas
            n_troca = randrange(0, 20)
            filho.genes[n_troca] = mae.genes[n_troca]
        return filho


class CromossomoFactory:
    
    @staticmethod
    def build():
        crom = Cromossomo
        crom.genes =  np.random.uniform(low=00, high=1, size=(20,))#random.sample(range(1 , 1000), 20)
        crom.aptidao = 0
        return crom