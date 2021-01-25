import bs4
from bs4 import BeautifulSoup
import requests

response = requests.get("https://codelearn.io/sharing/tan-gai-voi-machine-learning-nhu-the-nao")
html_doc = response.text
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())
result = soup.select("title")
for i in result:
    print(i.get_text())
test = soup.select("a")
print(test[0].get("href")) # get css ( Lấy theo css )