text = str(input())

Adenin = text.count("а") + text.count("А")
Guanin = text.count("г") + text.count("Г")
Cianin = text.count("ц") + text.count("Ц")
Timir = text.count("т") + text.count("Т")

print(f"Аденин: {Adenin}")
print(f"Гуанин: {Guanin}")
print(f"Цитозин: {Cianin}")
print(f"Тимин: {Timir}")

