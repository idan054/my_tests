#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = "https://www.telegram-group.com/%d7%97%d7%93%d7%a9%d7%95%d7%aa/%d7%9e%d7%9b%d7%95%d7%a8-%d7%9c%d7%97%d7%93%d7%a9%d7%95%d7%aa/"

news = "%d7%97%d7%93%d7%a9%d7%95%d7%aa".replace("%", "\\x")
news = bytes(news.replace("\\\\", "\\").encode())
print(type(news))
print(news)
word = news.decode('UTF-8')
print(word)


# print(type(news))
# print(news)
# news = bytes(news.encode())
# print(type(news))
# print(news)
# news = news.decode('UTF-8')
# print(type(news))
# print(news)

# word = "חדשות"
# print(word)
# word = word.encode('UTF-8')
# print(type(word))
# print(word)
#
# word = news.decode('UTF-8')
# print(word)
