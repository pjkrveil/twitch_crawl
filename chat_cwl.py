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

    	# get chatting logs
    	username_info = soup.find_all("button", {"class":"chat-line__username"})

    	# crawl list of user data
    	l_user_display_name = username_info.find_all("span", {"class":"chat-author__display-name"})
    	l_user_login_id = username_info.find_all("span", {"class":"chat-author__intl-login"})
    	l_user_chat_text = username_info.find_all("span", {"class":"text-fragment"})

    	# list for saving user data
    	user_display_name = []
    	user_login_id = []
    	user_id_color = []

    	for user_dp_name in l_user_display_name:
    		# extract user_display_name text data
    		user_display_name.append(user_dp_name.get_text())

    		# extract color values
    		color_val = (user_dp_name.split("(")[-1])[:-1]
    		user_id_color.append(color_val)

    	for user_login_id in l_user_login_id:
    		# extract user_login_id text data
    		user_login_id.append(user_login_id.get_text())

    	







