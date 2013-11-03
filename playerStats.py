from bs4 import BeautifulSoup
from array import *
import urllib2
import sys
import string
url="http://www.michigantechhuskies.com/sports/mice/2013-14/bios/anderson_patrick_nv62?view=gamelog"
page= urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
bio = "Player's Bio"
name = soup.findAll('div',{'class':'name'})
stats = soup.findAll('td',{'class':'align-center'})
count = 0
check  = 0
playername = ""
for eachname in name:
	playername = eachname
f = open('game.txt', 'w')
f.write(playername)
f.write("\n")
for eachstat in stats:
	f.write(eachstat)
	f.write(" ")
	count = count + 1
	check = check + 1
	if check == 12:
		f.write("\n")
		check = 0 	
f.close()
