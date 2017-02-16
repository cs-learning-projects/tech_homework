# 3
'''
Обратиться с странице https://habrahabr.ru/. 
Получить текст страницы. При помощи регулярных выражений 
нужно получить все ссылки со страницы на другие.
'''
import re

parsed_url = requests.get('https://habrahabr.ru/')
all_links = re.findall(r'href=[\'"]?([^\'" >]+)', parsed_url)
# эта строка в консоли выдавала сначала TypeError: expected string 
# or bytes-like object, почему? ведь указано raw в начале.
print(all_links)

'''
r'...' is a "raw" string. It stops you having to worry about escaping 
characters quite as much as you normally would. (\ especially -- in a 
raw string a \ is just a \. In a regular string you'd have to do \\ 
every time, and that gets old in regexps.)

"href=[\'"]?" says to match "href=", possibly followed by a ' or ". "
Possibly" because it's hard to say how horrible the HTML you're looking 
at is, and the quotes aren't strictly required.

Enclosing the next bit in "()" says to make it a "group", which means 
to split it out and return it separately to us. It's just a way to say 
"this is the part of the pattern I'm interested in."

"[^\'" >]+" says to match any characters that aren't ', ", >, or a space. 
Essentially this is a list of characters that are an end to the URL. 
It lets us avoid trying to write a regexp that reliably matches a full 
URL, which can be a bit complicated. 
'''
