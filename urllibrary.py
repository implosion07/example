import urllib.parse,urllib.error,urllib.request
a=urllib.request.urlopen("https://www.actvid.com/")
for l in a:
    print(l.decode().rstrip())