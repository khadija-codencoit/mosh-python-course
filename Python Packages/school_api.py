import requests
from datetime import datetime, timedelta
class Examppm:
    def __init__(self, email, password):
        self.token = None
        self.token_expires = None
        self.credencial = {
            "email": email,
            "password": password,
        }
        
        self.login_url = "https://api.exsppm.com/api/v1/login"
        self.home = "https://api.exsppm.com/api/v1/home"
 
    def login(self):
        login_resonse = requests.post(self.login_url, json=self.credencial)
        self.token_expires = datetime.now() + timedelta(hours=24)
        self.token = login_resonse.json()['data']['sppm_access_token']
        self.cookies = {
            "sppm_access_token": self.token
        }
        return self.token, self.token_expires
    def check_token(self):
        if self.token is None or datetime.now() > self.token_expires:
            self.login()

    
    def get_homepage_info(self):
        self.check_token()
        hompepage_response = requests.get(self.home,cookies=self.cookies)
        return hompepage_response.json()
    
homepage = Examppm("juhairfahmid@gmail.com", "1234")
homepage_data = homepage.get_homepage_info()
print(homepage_data["data"])