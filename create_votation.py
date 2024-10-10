from person import Person
from random import choice,randint,random,uniform

class CreateVotation:
    
    def __init__(self) -> None:
        self.persons = list()
        self.total_white_votes = 0
        self.no_voted = 0
        
    def create_persons_list(self,persona:Person):
        self.persons.append(persona)
    
    def calculate_white_votes(self,qnt):
        possibily = uniform(0.01,0.25)
        self.total_white_votes=(int(round(possibily*qnt)))

        
    def make_votations(self,qnt):
        self.calculate_white_votes(qnt)
        votes_no_white_votes =self.no_voted= qnt - self.total_white_votes
        for candidato in self.persons:
            votes_candidato = randint(0,votes_no_white_votes)
            candidato.number_votes += votes_candidato
            votes_no_white_votes-=votes_candidato
        self.no_voted = votes_no_white_votes
        return self.total_white_votes,self.no_voted
    
    
    def show_results(self):
        for canditato in self.persons:
            print(f'{canditato.name} - {canditato.partido} - {canditato.number_votes}')
        print(f'Total de votos brancos: {self.total_white_votes}')
        print(f'Votos anulados/sem origem: {self.no_voted}')

        
            
            
            
if __name__ == '__main__':
    votacao = CreateVotation()
    gabriel = Person('Gabriel','BR',99)
    dilma = Person('Dilma','PT',13)
    votacao.create_persons_list(gabriel)
    votacao.create_persons_list(dilma)
    votacao.make_votations(100)
    votacao.show_results()
            
            
            
        
    