import urllib.request
import re

def SaveImg(url, name):
    res = urllib.request.Request(url)
    res.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')

    page = urllib.request.urlopen(res)
    img = page.read()

    with  open(name, "wb") as f:
        f.write(img)


url = 'https://tieba.baidu.com/p/5106584395'

res = urllib.request.Request(url)
res.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')

cont = urllib.request.urlopen(res)

#print(cont.geturl())

page = cont.read()

html = page.decode('utf-8')

with open("PageContent.txt", "w", encoding='utf-8') as f:
    f.write(html)

imglist = re.findall(r'<img class="BDE_Image" src="([^"]+\.jpg)"',html)

for img in imglist:
    name = img.split('/')[-1]
    SaveImg(img, name)