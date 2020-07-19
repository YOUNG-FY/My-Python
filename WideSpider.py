import urllib.request as r
res = r.urlopen("http://www.fishc.com")
ht = res.read()
ht = ht.decode("utf-8")
print(ht)