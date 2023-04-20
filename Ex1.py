class Filme:
    def __init__(self,nome,duracao):
        self.nome = nome 
        self.duracao = duracao
        
    def play(self):
        print(f"o filme {self.nome} com duracao de {self.duracao} vai comecar...")
        

class Acao(Filme):
    def __init__(self, nome, duracao,categoria,faixa_etaria):
        super().__init__(nome, duracao,)
        self.categoria = categoria
        self.faixa_etaria = faixa_etaria
        
    def play(self):
        print(f"O filme {self.nome} e de {self.categoria} e leva {self.duracao}, contem tiros e explosao! Esse filme nao e indicado para menores de {self.faixa_etaria} anos")
    
    
class Suspense(Filme):
    def __init__(self, nome, duracao,categoria,faixa_etaria):
        super().__init__(nome, duracao)
        self.categoria = categoria
        self.faixa_etaria=faixa_etaria
        
    def play(self):
        print(f"O filme {self.nome} e de {self.categoria} e leva {self.duracao}, contem tensao e muito medo... Esse filme nao e indicado para menores de {self.faixa_etaria} anos")
        
class Terror(Filme):
    def __init__(self, nome, duracao,categoria,faixa_etaria):
        super().__init__(nome, duracao)
        self.categoria = categoria 
        self.faixa_etaria = faixa_etaria
        
    def play(self):
        print(f"O filme {self.nome} e de {self.categoria} e leva {self.duracao}, contem poder sobrenatural, violencia e medo... Esse filme nao e indicado para menores de {self.faixa_etaria} anos")
        
class Policial_Fantasia(Filme):
    def __init__(self, nome, duracao,categoria,faixa_etaria):
        super().__init__(nome, duracao)
        self.categoria = categoria
        self.faixa_etaria = faixa_etaria
    def play(self):
        print(f"O filme {self.nome} e de {self.categoria} e leva {self.duracao}, e baseado em fatos reais... Esse filme nao e indicado para menores de {self.faixa_etaria} anos")
        
class Romance(Filme):
    def __init__(self, nome, duracao,categoria,faixa_etaria):
        super().__init__(nome, duracao)
        self.categoria = categoria
        self.faixa_etaria = faixa_etaria
        
    def play(self):
        print(f"O filme {self.nome} e de {self.categoria} e leva {self.duracao} contem muito amor e paixao... Esse filme nao e indicado para menores de {self.faixa_etaria} anos")
        
    
            
    
    

    
film1= Filme("Velozes e Furiosos","2h e 50min")
film1.play()
film2=Acao("Top Gun","2h e 50 min","Acao",16)
film2.play()
film3=Suspense("Um lugar silencioso","3h","Suspense",18)
film3.play()
film4=Terror("Telefone Preto","2h e 30min","Terror",18)
film4.play()
film5=Policial_Fantasia("A espera de um milagre","3h","Drama",10)
film5.play()
film6 = Romance("A continencia do amor","2h e 02min","Romance","L")

    