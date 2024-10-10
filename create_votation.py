from person import Person
from random import choice,uniform
from typing import List

class CreateVotation:
    
    def __init__(self) -> None:
        self.persons:List[Person] = list()
        self.total_white_votes = 0
        
    def create_persons_list(self,persona:Person):
        self.persons.append(persona)
    
    def calculate_white_votes(self,qnt):
        possibily = uniform(0.01,0.25)
        self.total_white_votes=(int(round(possibily*qnt)))
        return self.total_white_votes

    def make_votations(self,qnt):
        self.calculate_white_votes(qnt)
        votes_remaining = qnt - self.total_white_votes
        while votes_remaining>0:
            candidato = choice(self.persons)
            candidato.number_votes+=1
            votes_remaining-=1
        return self.total_white_votes    
    
    def show_results(self):
        print('Resultados da eleição!')
        for canditato in self.persons:
            print(f'{canditato.name} - {canditato.partido} - {canditato.number_votes}')
        print(f'Total de votos brancos: {self.total_white_votes}')

        
if __name__ == '__main__':
    votacao = CreateVotation()
    gabriel = Person('Gabriel','BR',99)
    dilma = Person('Dilma','PT',13)
    aecio = Person('Aécio','PSDB',19)
    votacao.create_persons_list(gabriel)
    votacao.create_persons_list(dilma)
    votacao.create_persons_list(aecio)
    votacao.make_votations(100000)
    votacao.show_results()
