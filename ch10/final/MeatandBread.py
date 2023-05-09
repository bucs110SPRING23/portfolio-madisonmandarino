import requests
import random

class MeatandBread:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.spoonacular.com/food/products/search'

    def _get_products(self, query):
        query_params = {
            'apiKey': self.api_key,
            'query': query,
            'number': 100,
        }
        response = requests.get(self.base_url, params=query_params)
        response.raise_for_status()
        return response.json()['products']

    def get_random_meat(self):
        products = self._get_products('meat')
        meats = [product['title'] for product in products if 'meat' in product['title'].lower()]
        return random.choice(meats)

    def get_random_bread(self):
        products = self._get_products('bread')
        breads = [product['title'] for product in products if 'bread' in product['title'].lower()]
        return random.choice(breads)