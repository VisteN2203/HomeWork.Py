import math

kg = float(input("Сколько ты весишь?"))

print(f"Масса тела = {kg} кг")

print(f"Количество МГ реплагал = {kg * 0.2} мг")

print(f"Этап расчета (число флаконов) = {round((kg * 0.2) / 3.5,1)}")

print(f"Реально необходимое число флаконов = {math.ceil(round((kg * 0.2) / 3.5,1))}")
