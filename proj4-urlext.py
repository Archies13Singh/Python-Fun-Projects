from urllib.request import urlopen
# urllib is a Python module that can be used for opening URLs
page = urlopen("https://www.google.com")
print(page.headers)