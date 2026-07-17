import calendar 
import locale

locale.setlocale(locale.LC_TIME, "ptb")

ano = int(input("Digite o ano: "))
mes = int(input("Digite o mês: "))

print("\n", calendar.month(ano, mes))