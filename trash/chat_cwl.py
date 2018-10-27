import scrapy
import datetime
import sys
import os

from modules import *

class TwitchChatCrawler(scrapy.Spider):

	def __init__(self):
		name = 'chat_crawler'
		start_urls = getURL()
		prev_last_user_id = ""
		prev_last_chat_text = ""


	# Get URL for crawling : an user should type their twitch id for crawling chatting logs
	def getURL(self):
		twitch_id = raw_input("Enter your twitch ID (example : pjkrveil) : ")
		start_urls = 'https://www.twitch.tv/' + twitch_id

		return start_urls


	def parsePrevChat(self, response):
		page = response.url
		twitch_id = url.split("/")[-1]

		# targeting chat_log page
		crawl_page = response.css("div.tw-flex-grow-1 tw-full-height tw-pd-b-1")

		# crawl current chatting log state
		# including user_display_name(KR/EN), user_id(EN) and chat_text(all languages)
		user_display_name = chat_log.css("span.chat-author__display-name::text").extract()
		user_id = chat_log.css("span.chat-author__intl-login::text").extract()
		chat_text = chat_log.css("span.text-fragment::text").extract()

		return user_display_name, user_id, chat_text


	# Need modify
	def saveChatlog(self, response):
		# the time that starts 
		dt = datetime.datetime.now()

		# define the saving chatlog filename
		filename = 'chatlog-%s-%s%2d%2d_%2d%2d%2d.html' % twitch_id, \
		dt.year, int(dt.month), int(dt.day), int(dt.hour), int(dt.minute), int(dt.second)

		with open(filename, 'wb') as f:
			f.write(response.body)

	# check the update state of chatting logs
	def checkUpdate(self, response, user_id, chat_text):
		curr_last_user_id = user_id[-1]
		curr_last_chat_text = chat_text[-1]

		# return True if both arguments are equal
		cmp_id = (lambda x, y: x != y)(curr_last_user_id, self.prev_last_user_id)
		cmp_chat_text = (lambda x, y: x != y)\
		                (curr_last_chat_text, self.prev_last_chat_text)

		# should be True with that cmp_id and cmp_chat_text are True
		if cmp_id and cmp_chat_text:
			parsePrevChat(response)

		return user_display_name, user_id, chat_text
















