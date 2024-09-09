from abc import ABC, abstractmethod
import os
os.system("cls || clear") #Limpar terminal.

#Definicao de classes
class Endereco:
    def __init__(self, logradouro: str, numero: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade

    def __str__(self) -> str:
        return (f"\nLogradouro: {self.logradouro}" f"\nNumero: {self.numero}" f"\nCidade: {self.cidade}")

class Funcionario(ABC):
    def __init__(self, nome: str, email: str, salario: float, enderenco: Endereco) -> None:
        self.nome = nome
        self.email = email
        self.salario = float
        self.endereco = Endereco

    @abstractmethod
    def Salario_Final(float) -> float:
        pass

    def __str__(self) -> str:
        return (f"\nNome: {self.nome}" f"\nEmail: {self.email}" f"\nSalario: {self.salario}" f"\nEndereco: {self.endereco}")

class Motoboy(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, enderenco: Endereco, cnh: str) -> None:
        super().__init__(nome, email, salario, enderenco)
        self.cnh = cnh

    def Salario_Final(float) -> float:
        return 2000.0
        
