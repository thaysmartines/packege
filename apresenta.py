class PassagemAerea:
    def __init__(self, origem, destino, data, hora):
        self.origem = origem
        self.destino = destino
        self.data = data
        self.hora = hora

    def cadastrar(self):
        print("Cadastro de Passagem Aérea ")
        self.origem = input("Digite a origem: ")
        self.destino = input("Digite o destino: ")
        self.data = input("Digite a data (dd/mm/aaaa): ")
        self.hora = input("Digite a hora (hh:mm): ")
        print("{:=^100}".format("Cadastro de passagem realizada com sucesso!"))
        self.mostrar()
# mudança teste
    def mostrar(self):
        print("Dados da sua Passagem: ")
        print(f"Origem: {self.origem}")
        print(f"Destino: {self.destino}")
        print(f"Data: {self.data}")
        print(f"Hora: {self.hora}")

    def alterar(self):
        print("Alteração de Passagem Aérea")
        self.mostrar()
        self.origem = input("Digite a nova origem (ou deixe em branco para não alterar): ")
        self.destino = input("Digite o novo destino (ou deixe em branco para não alterar): ")
        self.data = input("Digite a nova data (dd/mm/aaaa) (ou deixe em branco para não alterar): ")
        self.hora = input("Digite a nova hora (hh:mm) (ou deixe em branco para não alterar): ")
        print("{:=^100}".format(" Passagem aérea alterada realizada com sucesso!"))
        self.mostrar()

    def excluir(self):
        self.origem = None
        self.destino = None
        self.data = None
        self.hora = None
        print("{:=^100}".format("Passagem aérea excluida!"))
        self.mostrar()

if __name__ == "__main__":
    passagem = PassagemAerea("", "", "", "")
    while True:
        print("\n Escolha uma opção:")
        print("1 - Cadastrar passagem aérea")
        print("2 - Alterar passagem aérea")
        print("3 - Excluir passagem aérea")
        print("4 - Sair")
        opcao = input()
        if opcao == "1":
            passagem.cadastrar()
        elif opcao == "2":
            passagem.alterar()
        elif opcao == "3":
            passagem.excluir()
        elif opcao == "4":
            break
        else:
            print("Opção inválida")
