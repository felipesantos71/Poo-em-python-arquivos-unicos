from enum import Enum
import os

from numpy import double
os.system("cls || clear")

#Definicao de classe
class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Setor(Enum):
    RECURSOS_HUMANOS = "Recursos Humanos"
    FINANCEIRO = "Financeiro"
    MARKETING = "Marketing"
    VENDAS = "Vendas"

class Funcionario:
    def __init__(self, id: int, nome: str, idade: int, salario: double, setor: Setor, sexo: Sexo) -> None:
        """Construtor."""
        self.id = id
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.setor = setor
        self.sexo = sexo

    def __str__(self) -> str:
        """Equivalente ao toString() do JAVA."""
        return (f"\nID: {self.id}"
                f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nSalario: {self.salario}"
                f"\nSetor: {self.setor.value}"
                f"\nSexo: {self.sexo.value}")
    
#Instanciando classe
funcionario_01 = Funcionario(23659, "Nestor", 56, 2000.0, Setor.MARKETING, Sexo.FEMININO)

print(funcionario_01)