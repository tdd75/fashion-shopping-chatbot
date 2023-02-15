import requests
import os


class WebService:
    def __init__(self):
        self.base_url = 'http://web:8000/api/v1'
        self.session = requests.session()
        self.token = self.get_token()
        self.session.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}',
        }

    def get_token(self):
        username = os.getenv('BOT_USERNAME')
        password = os.getenv('BOT_PASSWORD')
        if not username or not password:
            raise Exception('Error when load bot credentials')

        res = requests.post(self.base_url + '/auth/login/', json={
            'identify': username,
            'password': password,
        })
        if not res.ok:
            raise Exception('Error when get token')
        return res.json()['access']

    def get_product(self, query={}):
        res = self.session.get(self.base_url + '/products/', params=query)
        if not res.ok:
            raise Exception('Error when get product')
        return res.json()['results'][:5]


web_service = WebService()
