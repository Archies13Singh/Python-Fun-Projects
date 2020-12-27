import wikipedia
search = input("Search :")
query = wikipedia.page(search)
print(query.summary)
