import requests

class Crawler:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
		self.baseUrl = "https://www.instagram.com"
		self.loginUrl = self.baseUrl + "/accounts/login"       

	def login(self):
		session = requests.Session()
		csrf = session.get(self.loginUrl)
		loginCsrfToken = str(csrf.cookies)
		requestHeaders = {
							"origin":self.baseUrl,
							"accept-encoding": "gzip, deflate, br",
							"accept-language": "en-US,en;q=0.9",
							"user-agent": self.userAgent,
							"x-requested-with": "XMLHttpRequest",
							"x-csrftoken": loginCsrfToken,
							"x-instagram-ajax": "de81cb3fd9c4-hot",
							"content-type": "application/x-www-form-urlencoded",
							"accept": "*/*",
							"referer": "https://www.instagram.com/accounts/login"
		}
		login = session.post(self.loginUrl, data={"username": self.username, "password":self.password}, headers=requestHeaders)
		if 'authenticated": true,' in str(login.text):
c = Crawler("pythontest53", "testtest") 
c.login()
#i don't know what is wrong but the csrftoken doesn't seem to get fetched
