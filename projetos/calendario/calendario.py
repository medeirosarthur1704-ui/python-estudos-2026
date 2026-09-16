# ================================================================
# CALENDÁRIO
# Exibe o calendário de um mês/ano escolhido pelo usuário,
# usando o módulo padrão 'calendar' e mostrando os nomes dos
# meses/dias em português através do 'locale'.
# ================================================================

from time import sleep
import pyfiglet             # gera o banner em ASCII art
import calendar             # módulo padrão pra gerar calendários
import locale                # permite exibir datas em português

# Define o idioma do calendário como português do Brasil
locale.setlocale(locale.LC_TIME, "ptb")

# Banner de título, em amarelo
banner = pyfiglet.figlet_format("Calendário", font="slant")
print(f"\033[1;38;2;255;255;0m{banner}\n")

# Pede o ano e o mês que o usuário quer visualizar
ano = int(input("\033[1;38;2;255;140;0m \n[+] Digite o ano: "))
mes = int(input("\033[1;38;2;255;140;0m \n[+] Digite o mês: "))

# calendar.month(ano, mes) devolve o calendário do mês já formatado como texto
print(f"\033[1;38;2;255;20;147m\n{calendar.month(ano, mes)}")