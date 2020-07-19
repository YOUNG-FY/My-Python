import re

print(1, re.search(r"james", "james and wade."))  

#通配符.
print(2, re.search(r"jam..", "james and wade."))
print(2, re.search(r"\.", "james and wade.")) 
print(2, re.search(r"[.]", "james and wade."))  

print(3, re.search(r"\d", "james and 1 wade."))  
print(4, re.search(r"\s", "james and 1 wade."))
print(4, re.findall(r'\n', "james and abc wade.\n"))

print(5, re.search(r"[hahe]", "james and 1 wade."))  

print(6, re.search(r'[a-z]', "james and abc wade."))
print(6, re.findall(r'[a-c]', "james and abc wade."))
#相对上一个取反
print(6, re.findall(r'[^a-c]', "james and abc wade."))

print(7, re.search(r"1[1-9]", "james and 123 wade.")) 

#d可以是3-10的重复
print(8, re.search(r"sd{3,10}f", "asddddddfe"))
#？匹配子表达式0或1次， +匹配>=1次， *匹配>=0次
print(8, re.search(r"(sd?f)(sd?f)", "asfsdfe"))
print(8, re.search(r"(sd+f)(sd+f)", "asdfsddddfe"))
print(8, re.search(r"(sd*f)(sd*f)", "asfsddddfe"))

#匹配一个0-255的数
print(9, re.search(r"[0-1]\d\d|2[0-4]\d|25[0-5]", "3188"))

#匹配ip地址
print(10, re.search(r"(([0-1]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([0-1]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])", "10.13.160.4"))
#非捕获符?:
print(10, re.findall(r"(([0-1]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([0-1]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])", "10.13.160.4"))
print(10, re.findall(r"(?:(?:[0-1]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}(?:[0-1]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])", "10.13.160.4"))

#^表示从字符串开始来匹配，注意与/A的区别
print(11, re.search(r"^james", "1 james and wade."))

#$表示匹配到字符串的结尾，注意与/Z的区别
print(12, re.search(r"$wade", "1 james and wade."))

print(13, re.search(r"(james)(wade)\2", "1 jame swadewade"))
print(14, re.search(r"(james)\1", "jamesjames and wade"))

#\后3位或0开头表示八进制的ASCII码值，比如\060等于十进制的ASCII码值为48，即为0
print(15, re.search(r"(james)\060", "james0 and wade"))

#贪婪与非贪婪
print(16, re.search(r"(sd.+e)", "asfsddeddfe"))
print(16, re.search(r"(sd.+?e)", "asfsddeddfe"))

#\b用于匹配单词边界
print(17, re.search(r"\bjames\b", "james and wade james_."))
print(17, re.search(r"\bjames\b", "(james) and  wade."))
print(17, re.search(r"\bjames\b", "james_ and wade."))

#\B用于匹配非单词边界
print(18, re.search(r"james\B", "james_ and wade.")) 