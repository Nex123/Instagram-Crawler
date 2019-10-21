import requests
import json
import re
from bs4 import BeautifulSoup

class Crawler:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.baseUrl = "https://www.instagram.com"
		self.loginUrl = self.baseUrl + "/accounts/login"
		self.userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"
		self.loginData = {
						"username": self.username,
						"password": self.password
		}
		self.csrfToken = None

	def getCsrfToken(self):
		with requests.Session() as s:
			s.headers = {"user-agent": self.userAgent}
			s.headers.update({"Referer": self.baseUrl})

			get = s.get(self.baseUrl)

			soup = BeautifulSoup(get.content, "html.parser")
			body = soup.find("body")

			js = body.find("script", text=re.compile("window._sharedData"))
			js = js.get_text().replace("window._sharedData = ", "")[:-1]
			jsonData = json.loads(js)
			self.csrfToken = jsonData["config"]["csrf_token"]
			return self.csrfToken
