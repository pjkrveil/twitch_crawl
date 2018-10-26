import sys
import os

def getURL():
	twitch_id = raw_input("Enter your twitch ID (example : pjkrveil) : ")
	start_urls = 'https://www.twitch.tv/' + twitch_id

	return start_urls