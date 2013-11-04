from bs4 import BeautifulSoup
import urllib
import os

def send_to_file(player_full_name, title_bar, stats):
	file_to_write = open('the_stats.txt', 'w')
	file_to_write.write(player_full_name + '\n')
	file_to_write.write(title_bar + '\n')
	file_to_write.write(stats + '\n')
	file_to_write.close()


def player_name():
	url = 'http://www.michigantechhuskies.com/sports/mice/2013-14/bios/anderson_patrick_nv62?view=gamelog'
	soup = BeautifulSoup(urllib.urlopen(url).read())
	close = False
	count = 0
	player_full_name = ''
	for name in soup.find_all('span',{'class':'name'}):
		count += 1
		if(count == 1):
			name = name.string
			player_full_name = name
	return player_full_name

def player_stats():
	#Get the player stats and print to file
	url = 'http://www.michigantechhuskies.com/sports/mice/2013-14/bios/anderson_patrick_nv62?view=gamelog'
	soup = BeautifulSoup(urllib.urlopen(url).read())
	close = False
	count = 0
	tabs = '\t'
	array_stats = []
	for games in soup.find_all('tr',{'class':'odd'}):
		for stats in soup.find_all('td',{'class':'align-center'}):
			count += 1
			if(count == 2):
				stats = stats.string.replace(' ', '')
				stats = stats.replace('\n','')
				array_stats.append(stats)
			if (count == 3):
				stats = stats.string.replace(' ', '')
				stats = stats.replace('\n','')
				array_stats.append(stats)
			if (count == 4):
				stats = stats.string.replace(' ', '')
				stats = stats.replace('\n','')				
				array_stats.append(stats)
			if (count == 5):
				stats = stats.string.replace(' ', '')
				stats = stats.replace('\n','')				
				array_stats.append(stats)
			if (count == 6):
				stats = stats.string.replace(' ', '')
				stats = stats.replace('\n','')				
				array_stats.append(stats)
			if (count == 7):
				stats = stats.string.replace(' ', '')
				stats = stats.replace('\n','')				
				array_stats.append(stats)
			if (count == 8):
				stats = stats.string.replace(' ', '')
				stats = stats.replace('\n','')				
				array_stats.append(stats)
			if (count == 9):
				stats = stats.string.replace(' ', '')
				stats = stats.replace('\n','')				
				array_stats.append(stats)
			if (count == 10):
				stats = stats.string.replace(' ', '')
				stats = stats.replace('\n','')				
				array_stats.append(stats)
			if (count == 11):
				stats = stats.string.replace(' ', '')
				stats = stats.replace('\n','')				
				array_stats.append(stats)
			if (count == 12):
				stats = stats.string.replace(' ', '')
				stats = stats.replace('\n','')				
				array_stats.append(stats)
	return array_stats

def main():
	tabs = '\t'
	title_bar = ('G%sA%sPTS%sPIM%s+/-%sPPG%sSHG%sENG%sGWG%sGTG%sS' % (tabs,tabs,tabs,tabs,tabs,tabs,tabs,tabs,tabs,tabs))

	stats = ''
	#call player_name()
	player_full_name = player_name()


	#call player stats
	tabs = '\t'
	array_stats = player_stats()
	for elements in array_stats:
		elements = str(elements)
		stats += elements.strip('\r')
		stats += tabs

	#send everything to be written to a file
	send_to_file(player_full_name, title_bar, stats)

if __name__ == '__main__':
	main()
