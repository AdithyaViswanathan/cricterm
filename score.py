from tabulate import tabulate
from bs4 import BeautifulSoup
from sys import stdout
import requests
import time
import os
printer=""
# printer=''''''
# printer="What os \n\n"
# printer+="THat is wa\n\n"
# printer+="seri da dei\n\ns"

def first(printer,URL):
	url = URL
	req = requests.get(url)
	soup = BeautifulSoup(req.text,"html.parser")
	Title = soup.title.string[:-15]
	printer+=Title+"\n"
	BatHead = []
	BowlHead = []
	BatStats = []
	BowlStats = []
	flag = 0
	for x in soup.findAll("div",{"class":"cb-scrs-wrp"}):
		for y in x.findAll("div"):
			printer+=y.text
	for x in soup.findAll("div",{"class":"cb-min-inf"}):
		flag+=1
		for y in x.findAll("div",{"class":"cb-bg-gray"}):
			for z in y.findAll("div"):
				if(flag==1):
					BatHead.append(z.text)
				else:
					BowlHead.append(z.text)
		for y in x.findAll("div",{"class":"cb-min-itm-rw"}):
			for z in y.findAll("div"):
				if(flag==1):
					BatStats.append(z.text)
				else:
					BowlStats.append(z.text)
	printer+="\n"
	printer+=tabulate([BatStats[0:6],BatStats[6:]], headers=BatHead, tablefmt='fancy_grid')
	printer+="\n"
	printer+=tabulate([BowlStats[0:6],BowlStats[6:]], headers=BowlHead, tablefmt='fancy_grid')
	printer+="\n"
	
	for x in soup.findAll("div",{"class":"cb-min-rcnt"}):
		printer+=x.text
	printer+="\n"

	KeyStats = "KeyStats:"+"\n"
	for x in soup.findAll("div",{"class":"cb-key-lst-wrp"}):
		for y in x.findAll("div",{"class":"cb-min-itm-rw"}):
			KeyStats+=y.text+"\n"
	printer+=KeyStats

	for x in soup.find("p",{"class":"cb-com-ln"}):
		printer+=str(x).replace("<b>","").replace("</b>","")
	return printer

os.system("clear")
def initial(printer):
	url = "https://www.cricbuzz.com/"
	req = requests.get(url)
	soup = BeautifulSoup(req.text,"html.parser")
	for x in soup.findAll("div",{"class":"videos-list-carousal"}):
		for y in x.find_all("a",href=True):
			printer.update({str(y.text):str(y['href'])})
	return printer
			

def main():
	printer = {}
	menu = {}
	printer = initial(printer)
	selection = -1
	URL = ""
	while True:
		try:
			flag = 1
			for x,y in printer.items():
				menu.update({str(flag):x})
				flag+=1
			if(selection == -1):
				for x,y in menu.items():
					print(str(x) + " : " + y)
				selection = input()
				URL  = "https://www.cricbuzz.com" + printer[menu[selection]]
				os.system("clear")
			scoreboard = ""
			scoreboard = first(scoreboard,URL)
			print(f'\r'+scoreboard,end='',flush=True)
			print("\n\n\n\n")
			time.sleep(15)
			os.system("clear")


		except KeyboardInterrupt:
			selection = -1
main()


