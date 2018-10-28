from bs4 import BeautifulSoup

import requests

# Get URL for crawling : an user should type their twitch id for crawling chatting logs
def getURL():
	twitch_id = raw_input("Enter your twitch ID (example : pjkrveil) : ")
	start_urls = "https://www.twitch.tv/" + twitch_id

	return start_urls


def parseData(start_urls)
	with open(start_urls) as fp:
    	soup = BeautifulSoup(fp, 'html.parser')