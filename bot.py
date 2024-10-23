from botcity.core import DesktopBot
from botcity.maestro import *
import tkinter as tk
from interface import App

import os
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()
    relativo = r'dist\interface.exe'
    caminho = os.path.abspath(relativo)


    bot.execute(caminho)


    nome = ["Mari", "Vini", "Luis"]
    matricula = ["123", "456", "789"]

    for i in range(3):
        bot.wait(2000)
        # PREENCHER NOME E MATRICULA
        if not bot.find("nome", matching=0.97, waiting_time=10000):
            not_found("nome")
        bot.click_relative(102, 9)
        bot.backspace        
        bot.type_keys(nome[i])

        bot.tab()
        bot.type_keys(matricula[i])

        # FUNCIONARIO HORISTA
        if i==0:
            if not bot.find("horista", matching=0.97, waiting_time=10000):
                not_found("horista")
            bot.click_relative(-11, 7)
            
            bot.wait(500)

            if not bot.find("horas_trabalhadas", matching=0.97, waiting_time=10000):
                not_found("horas_trabalhadas")
            bot.click_relative(127, 8)
            bot.type_keys('160')

            bot.tab()
            bot.type_keys('25')

        # FUNCIONARIO FIXO
        elif i==1:
            if not bot.find("fixo", matching=0.97, waiting_time=10000):
                not_found("fixo")
            bot.click_relative(-11, 5)

            bot.wait(500)

            if not bot.find("salario", matching=0.97, waiting_time=10000):
                not_found("salario")
            bot.click_relative(129, 9)    
            bot.type_keys('3500')

        # FUNCIONARIO COMISSIONADO
        else:
            if not bot.find("comissionado", matching=0.97, waiting_time=10000):
                not_found("comissionado")
            bot.click_relative(-10, 5)

            bot.wait(500)

            if not bot.find("salario_base", matching=0.97, waiting_time=10000):
                not_found("salario_base")
            bot.click_relative(133, 6)
            bot.type_keys('2000')

            bot.tab()
            bot.type_keys('8000')
            
            bot.tab()
            bot.type_keys('15')

        # CALCULAR SALARIO
        if not bot.find("calcular_salario", matching=0.97, waiting_time=10000):
            not_found("calcular_salario")
        bot.click()
    
        # CONFIRMACAO
        bot.wait(2000)
        if not bot.find("confirmacao", matching=0.97, waiting_time=10000):
            not_found("confirmacao")
        bot.click()
        
        

    #FECHAR
    if not bot.find("fechar", matching=0.97, waiting_time=10000):
        not_found("fechar")
    bot.click()
    

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()