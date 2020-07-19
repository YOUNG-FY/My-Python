import urllib.request 
import urllib.parse
import json

#url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

content = str(input("Please input the sentence to be translated:"))

header = dict()
header['user-agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"

data = dict()
data["i"] = content
data["from"] = "AUTO"
data["to"] = "AUTO"
data["client"] = "fanyideskweb"
data["salt"] = "15941326045464"
data["sign"] = "4ff07afd1ef6e62b040e46bf0b6a2eed"
data["ts"] = "1594132604546"
data["bv"] = "02a6ad4308a3443b3732d855273259bf"
data["doctype"] = "json"
data["version"] = "2.1"
data["keyfrom"] = "fanyi.web"
data["action"] = "FY_BY_CLICKBUTTION"

data = urllib.parse.urlencode(data).encode("utf-8")

res = urllib.request.Request(url, data, header)
html = urllib.request.urlopen(res)

print(res.headers)
page = html.read().decode("utf-8")

target = json.loads(page)

print("the result is:%s" % target["translateResult"][0][0]["tgt"])