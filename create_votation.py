from person import Person
from random import choice,randint,random,uniform

class CreateVotation:
    
    def __init__(self) -> None:
        self.persons = list()
        self.calculate_white_votes = 0
        
    def create_persons_list(self,persona:Person):
        self.persons.append(persona)
    
    @staticmethod    
    def calculate_white_votes(qnt):
        possibily = uniform(0.01,0.25)
        return possibily

        
    def make_votations(self,qnt):
        white_votes = int(round(self.calculate_white_votes(qnt) * qnt))
        votes = qnt - white_votes
        for candidato in self.persons:
            
            votes_candidato = candidato.number_votes=  randint(0,votes)
            print(candidato.number_votes)
            votes_candidato-=votes
            
        print(f'A porcentagem de votos brancos é: {int(round(white_votes*100/qnt))}%')
        print(white_votes,votes)
        return white_votes
    
    
    def show_results(self):
        for canditato in self.persons:
            print(f'{canditato.name} - {canditato.partido} - {canditato.number_votes}')
        
            
            
            
if __name__ == '__main__':
    votacao = CreateVotation()
    gabriel = Person('Gabriel','BR',99)
    dilma = Person('Dilma','PT',13)
    votacao.create_persons_list(gabriel)
    votacao.create_persons_list(dilma)
    votacao.make_votations(100)
    votacao.show_results()
            
            
            
        
    