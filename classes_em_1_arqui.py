from abc import ABC, abstractmethod
import os

class Endereco:
    def __init__(self, logradouro: str, numero: int, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self) -> str:
        return (f"\nLogradouro: {self.logradouro}" f"\nNumero: {self.numero}" f"\nComplemento: {self.complemento}" f"\nCEP: {self.cep}" f"\nCidade: {self.cidade}")

class Funcionario:
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    @abstractmethod
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return (f"\nNome: {self.nome}" 
                f"\nTelefone: {self.telefone}" 
                f"\nEmail: {self.email}"
                f"\nSalario: {self.salario_final()}"
                f"\nEndereco: {self.endereco}")

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crea: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea

    def salario_final(self) -> float:
        return 2000.0
    
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCrea: {self.crea}")
    
class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crm: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm
  
    def salario_final(self) -> float:
        return 3000.0
    
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCrm: {self.crm}")

Engenheiro01 = Engenheiro("Nestor", "(71)99988-8898", "nestorcervero@bol.com", Endereco("Rua X", 65, "Proximo ao Q", "41630-330", "Salvador"), "2654646")
Medico01 = Medico("Vania", "(71)99988-8898", "vaniacervero@bol.com", Endereco("Rua L", 45, "Proximo ao A", "41630-330", "Salvador"), "2654646")
print(Engenheiro01)
print(Medico01)