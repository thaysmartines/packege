
class PassagemArea:
      
    def cadastrar(self):
        print("Cadastro de Passagem Aérea")
        self.origem = input("Digite a origem: ")
        self.destino = input("Digite o destino: ")
        self.data = input("Digite a data (dd/mm/aaaa): ")
        self.hora = input("Digite a hora (hh:mm): ")
        print("Passagem aérea cadastrada com sucesso!")
        
        # mudança teste 2
    def alterar_preco(self, novo_preco):
        self.preco = novo_preco
    
    def escolher_assento(self, novo_assento):
        self.assento = novo_assento
        
        
class PassagemAviao(PassagemAerea):
    def __init__(self, preco, assento, portao_de_embarque, checkin):
        super().__init__(preco, assento)
        self.portao_de_embarque = portao_de_embarque
        self.checkin = checkin
    
    def decolar(self):
        print("O avião está decolando!")
    
    def abastecer(self):
        print("Abastecendo o avião.")
        
        
class PassagemBus(Passagem):
    def __init__(self, preco, assento, placa, leito):
        super().__init__(preco, assento)
        self.placa = placa
        self.leito = leito
    
    def abrir_porta(self):
        print("Abrindo a porta do ônibus.")
    
    def fechar_porta(self):
        print("Fechando a porta do ônibus.")
