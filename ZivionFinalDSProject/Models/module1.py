from urllib.request import urlopen

link = "https://tradingeconomics.com/country-list/rating"

f = urlopen(link)
myfile = f.read()
print(myfile)