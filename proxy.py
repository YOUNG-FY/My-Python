import urllib.request

url = "http://www.whatismyip.com.tw"

# handler = urllib.request.ProxyHandler({"http":"119.6.144.73:81"})

# opener = urllib.request.build_opener(handler)
# opener.addheaders = [("user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")]

# urllib.request.install_opener(opener)

res = urllib.request.urlopen(url)
page = res.read().decode("utf-8")

print(page)