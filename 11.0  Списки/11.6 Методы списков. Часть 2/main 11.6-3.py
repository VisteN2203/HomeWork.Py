text = str(input())

listText = text.lower().split()

articles = ['a', 'an', 'the']

total = listText.count(articles[0]) + listText.count(articles[1]) + listText.count(articles[2])

print(f"Общее количество артиклей: {total}")
