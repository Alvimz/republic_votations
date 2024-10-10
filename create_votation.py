from person import Person
from random import choice,randint,random,uniform

class CreateVotation:
    
    def __init__(self) -> None:
        self.persons = list()
        
    def create_persons_list(self,persona:Person):
        self.persons.append(persona)
    
    @staticmethod    
    def white_votes(qnt):
        possibily = uniform(0.01,0.25)
        return possibily

        
    def make_votations(self,qnt):
        white_votes = int(round(self.white_votes(qnt) * qnt))
        print(f'A porcentagem de votos brancos é: {int(round(white_votes*100/qnt))}%')
        print(white_votes)
            
            
            
            
if __name__ == '__main__':
    votacao = CreateVotation()
    gabriel = Person('Gabriel','BR',99)
    votacao.create_persons_list(gabriel)
    votacao.make_votations(100)
            
            
            
        
    