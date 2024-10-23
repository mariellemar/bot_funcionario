from abc import ABC, abstractmethod

import calendar

class Funcionario():
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula


    @abstractmethod
    def calcular_salario(self):
        pass


class FuncionarioHora(Funcionario):
    def __init__(self, nome, matricula, horas_trabalhadas, valor_hora):
        if horas_trabalhadas < 0 or valor_hora < 0:
            raise ValueError("Horas trabalhadas e valor por hora devem ser positivos")
        self.__horas_trabalhadas = horas_trabalhadas
        self.__valor_hora = valor_hora
        super().__init__(nome, matricula)

    
    def calcular_salario(self):
        salario_total = self.__horas_trabalhadas * self.__valor_hora
        return salario_total
    

class FuncionarioFixo(Funcionario):
    def __init__(self, nome, matricula, salario_mensal):
        if salario_mensal < 0:
            raise ValueError("Salario deve ser positivo")
        self.__salario_mensal = salario_mensal
        super().__init__(nome, matricula)


    def calcular_salario(self):
        return self.__salario_mensal
    

class FuncionarioComissao(Funcionario):
    def __init__(self, nome, matricula, salario_base, vendas, taxa_comissao):
        if salario_base <0 or vendas < 0 or taxa_comissao < 0:
            raise ValueError("Vendas e taxa de comissão devem ser positivos")
        self.__salario_base = salario_base
        self.__vendas = vendas
        self.__taxa_comissao = taxa_comissao
        super().__init__(nome, matricula)


    def calcular_salario(self):
        salario_total = self.__salario_base +(self.__vendas * (self.__taxa_comissao)/100)
        return salario_total
    

class FuncionarioProjeto(Funcionario):
    def __init__(self, nome, matricula, valor_projeto):
        self.__valor_projeto = valor_projeto
        super().__init__(nome, matricula)

    def calcular_salario(self):
        return self.__valor_projeto


def simular_pagamentos_horista(funcionario_hora, ano, mes, feriados):
    dias_trabalhados = 0

    for dia in range(1, calendar.monthrange(ano, mes)[1] + 1):
        dia_semana = calendar.weekday(ano, mes, dia)
        if dia_semana < 5 and dia not in feriados:  # Dias úteis (segunda a sexta) e não feriados
            dias_trabalhados += 1

    horas_trabalhadas_no_mes = dias_trabalhados * 8
    funcionario_hora.__horas_trabalhadas = horas_trabalhadas_no_mes  # Atualiza horas trabalhadas
    return funcionario_hora.calcular_salario()

# # Exemplo
# feriados = [7, 12]
# funcionario_hora = FuncionarioHora("Mari", "0000011111", 60, 45)
# salario_hora_mes = simular_pagamentos_horista(funcionario_hora, 2024, 10, feriados)
# print(salario_hora_mes)



# funcionario_hora = FuncionarioHora("Mari", "0000011111", 60, 45)
# salario_hora = funcionario_hora.calcular_salario()
# print(salario_hora)


# funcionario_fixo = FuncionarioFixo("Vini", "00000022222", 2000)
# salario_fixo = funcionario_fixo.calcular_salario()
# print(salario_fixo)


# funcionario_comissao = FuncionarioComissao("Eli", "0000033333", 1000, 1800, 15)
# salario_comissao = funcionario_comissao.calcular_salario()
# print(salario_comissao)
