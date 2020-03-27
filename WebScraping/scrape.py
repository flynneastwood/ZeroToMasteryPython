import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/") #Downloads the html
res2 = requests.get("https://news.ycombinator.com/news?p=2")
soup = BeautifulSoup(res.text, "html.parser")	#Parse to html
soup2 = BeautifulSoup(res2.text, "html.parser")

links = soup.select(".storylink")
links2 = soup.select(".storylink") #Examples of selecting CSS classes
subtext= soup.select(".subtext")
subtext2= soup.select(".subtext")
votes = soup.select(".score") 

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key= lambda k:k["votes"], reverse=True) # get a list from top likes to less.

def create_custom_hn(links, subtext): # Making information readable.
	hn = []
	for idx, item in enumerate(links):
		title = item.getText()
		href = item.get("href", None)
		vote = subtext[idx].select(".score")
		if len(vote):
			points = int(vote[0].getText().replace(" points", ""))
			if points > 99: 		 # if more than 99 votes, add to list
				hn.append({"title": title, "link": href, "votes": points})
	return sort_stories_by_votes(hn)
	return hn

pprint.pprint(create_custom_hn(mega_links, mega_subtext))


