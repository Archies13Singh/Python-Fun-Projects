from urllib.request import urlopen

page = urlopen("https://www.google.com")

sourcecode = page.read()
print(sourcecode)