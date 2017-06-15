# import librabries, BeautifulSoup = bs4
import urllib2
from bs4 import BeautifulSoup

#create var for page url
quote_page = 'http://www.bloomberg.com/quote/SPX:IND'

#query website from quote_page var, return html to var page
page = urllib2.urlopen(quote_page)

#parse html using BeautifulSoup and store in var 'soup'
soup = BeautifulSoup(page, 'html.parser')

#take out the <div> of name and get its value
name_box = soup.find('h1', attrs={'class': 'name'})

name = name_box.text.strip() #use strip() to remove starting and trailing
print name

#get index price
price_box = soup.find('div', attrs={'class': 'price'})
price = price_box.text
print price
