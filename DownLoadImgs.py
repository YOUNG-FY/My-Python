import urllib.request

def SaveImg(url, name):
    res = urllib.request.Request(url)
    res.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')

    page = urllib.request.urlopen(res)
    img = page.read()

    with  open(name, "wb") as f:
        f.write(img)


url = 'http://jandan.net/ooxx/MjAyMDA3MDgtMTI5#comments'

res = urllib.request.Request(url)
res.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')

cont = urllib.request.urlopen(res)

#print(cont.geturl())

page = cont.read()

html = page.decode('utf-8')

# with open("PageContent.txt", "w", encoding='utf-8') as f:
#     f.write(html)
index = 0
for i in range(100):
    start = html.find('img src')

    if start == -1:
        break

    raw = html[start:start+100]
    end = raw.find('.jpg')
    if end == -1:
        break

    ads = str('http:') + html[start+9 : start + end +4]
    print(ads)

    name = "{0} {1} {2}".format("图像", str(index), ".jpg")

    SaveImg(ads, name)
    index += 1

    html = html.replace('img src', "切换下一张图", 1)

