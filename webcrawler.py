import requests
from bs4 import BeautifulSoup

def trade_spider(url,element,classname):
	source = requests.get(url)
	text = source.text
	soup = BeautifulSoup(text,"html.parser")
	for link in soup.findAll(element,{'class':classname}):
		content=link.string
		linkid = link.get('href')
		print(content+"\n")
		print(linkid+"\n")

url=input("Enter the url of the site to be crawled : ")
element=input("enter the element from which data is needed (like a,div etc) : ")
classname=input("enter the class name : ")
trade_spider(url,element,classname)
