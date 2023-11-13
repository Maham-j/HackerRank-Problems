
n = int(input())
phoneBook = {}

for _ in range(n):
    name, phone_number = input().split()
    phoneBook[name] = phone_number

queries = []
try:
    while True:
        query = input()
        if not query:
            break
        queries.append(query)
except EOFError:
    pass

for query in queries:
    if query in phoneBook:
        print(f"{query}={phoneBook[query]}")
    else:
        print('Not found')
