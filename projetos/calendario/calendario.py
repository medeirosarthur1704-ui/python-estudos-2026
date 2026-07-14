import calendar
import locale

locale.setlocale(locale.LC_TIME, ("ptb"))

ano = int(input("Digite o Ano: "))
mes = int(input("Digite o Mês: "))

print("\n", calendar.month(ano, mes))