class Ingresso:
    def __init__(self,preco,setor) -> None:
        self.preco = preco 
        self.setor = setor 
        
    def alterar_preco(self,novo_preco):
        self.preco = novo_preco
        
    def mostrar_setor(self):
        print(f"Setor: {self.setor}")
        
class Ingresso_Vip(Ingresso):
    def __init__(self, preco, setor,camarote,open_bar,open_food,estacionamento) -> None:
        super().__init__(preco, setor)
        self.camarote = camarote
        self.open_bar = open_bar
        self.open_food = open_food
        self.estacionamento = estacionamento
        
    def pegar_bebida(self):
        if self.open_bar:
            print("Fique a vontade, pode escolher seu drink")
        else:
            print("Esse ingresso não possui Open bar")
        
    def acessar_camarote(self):
        if self.camarote:
            print("Pode acessar o camarote")
        else:
            print("esse ingresso nao acessa o camarote ")
    

pessoa1=Ingresso()


        