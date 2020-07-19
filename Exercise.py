
import math

class Turtle:
    color = "green"
    weight = 10

    def __add__(self, rhs):
        return self.color + rhs
    def climb(self):
        print("I am climbing!")
    def setName(self, name):
        self.name = name
        print("My name is %s" % self.name)

class newint(int):
    def __add__(self, rhs):
        return int.__add__(self, rhs)


# num = 100
# while num < 1000:
#     if(math.pow(num%10,3) + math.pow(num//10%10, 3) + math.pow(num//100%10, 3) == num):
#         print(num)
#     num += 1

# d={'k1':'v1','k2':[1,2,3], ('k','3'):{1, 2, 3}}
# for k, v in d.items():
#     if type(v) == list:
#         print(k)

# class Fibs:
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         return self.a

# f = Fibs()
# for each in f:
#     if each < 100:
#         print(each)
#     else:
#         break
import re

print(re.search('"james"', 'I like "james" and "wade"'))