import urllib.request as r

#res = r.Request("http://placekitten.com/g/1920/1080")
res = r.Request("http://wx3.sinaimg.cn/mw600/0076BSS5ly1ggjwnr6hd4j31900u0gq1.jpg")

page = r.urlopen(res)

print(page.geturl())
# print(page.info())
# print(page.getcode())

cat_img = page.read()

with  open("cat_1920_1080.gif", "wb") as f:
    f.write(cat_img)