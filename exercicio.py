class PassagemAerea:
    def __init__(self, origem, destino, data, hora):
        self.origem = origem
        self.destino = destino
        self.data = data
        self.hora = hora

    def cadastrar(self):
        print("Cadastro de Passagem Aérea")
        print("Origem: ", self.origem)
        print("Destino: ", self.destino)
        print("Data: ", self.data)
        print("Hora: ", self.hora)

    def alterar(self):
        self.origem = input("Digite a nova origem: ")
        self.destino = input("Digite o novo destino: ")
        self.data = input("Digite a nova data: ")
        self.hora = input("Digite a nova hora: ")
        print("Passagem Aérea alterada com sucesso!")
        self.cadastrar()

    def excluir(self):
        self.origem = None
        self.destino = None
        self.data = None
        self.hora = None

        print("Passagem Aérea excluída com sucesso!")

if __name__ == "__main__":
    passagem = PassagemAerea("São Paulo", "Rio de Janeiro", "01/04/2023", "08:00")
    

    passagem.cadastrar()

    passagem.alterar()

    passagem.excluir()
