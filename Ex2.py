class Pessoa:
    def __init__(self, matricula, nome, idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade, n1,n2,n3):
        super().__init__(matricula, nome, idade)
        self.n1 = n1 
        self.n2 = n2
        self.n3 = n3
        self.media = 0
    
    def get_media(self):
        media =  (self.n1 + self.n2 + self.n3 )/3
        if media >=7:
           print("Aprovado")
        elif media ==5:
            print("Esta de exame")
        else:
            print("Reprovado")
    
    def estudar(self):
        print(f"{self.nome} está estudando...")

class Professor(Pessoa):
    def __init__(self, matricula, nome, idade, formacao, disciplina, carga_horaria, salario):
        super().__init__(matricula, nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.carga_horaria = carga_horaria
        self.salario = salario
    
    def lecionar(self):
        print(f"{self.nome} está lecionando {self.disciplina} e SOFRENDO COM A CARGA HORARIA DE {self.carga_horaria}HR mas pelo menos está ganhandp R${self.salario}")


alun= Aluno("2022016","Thays Martines",20,10,5,9)
alun.get_media()
alun.estudar()

pro=Professor("20205669","Thiago",36,"Tecnologia","POO",200,12000)
pro.lecionar()