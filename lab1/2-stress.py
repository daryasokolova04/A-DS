import requests
from bs4 import BeautifulSoup
import re
import time

def get_text(url):
    page = requests.get(url)
    root = BeautifulSoup(page.content, 'html.parser')
    article = root.get_text()
    return article

text = get_text("https://ru.wikipedia.org/wiki/Стресс")
text = re.findall('[a-zа-яё]+', text, flags=re.IGNORECASE)
total_count = len(text)

data = []
file = open("Stress.txt", 'r')
for line in file:
    data += line.split(sep=None)


start = time.time()

res = 0
for i in range(0, len(data) - 2):
    for j in range(0, len(text) - 2):
        if data[i] + data[i+1] + data[i+2] == text[j] + text[j+1] + text[j+2]:
            res += 3

print("Процент плагиата: {}".format(round(res / total_count * 100, 2)))

end = time.time()
#print(end - start) #10.619821786880493