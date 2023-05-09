import requests
import random

class CheeseandSauces:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.nal.usda.gov/fdc/v1/foods/search'

    def _get_foods(self, query):
        query_params = {
            'api_key': self.api_key,
            'query': query,
            'pageSize': 200,
            'requireAllWords': 'true'
        }
        response = requests.get(self.base_url, params=query_params)
        response.raise_for_status()
        return response.json()['foods']

    def get_random_sauce(self):
        foods = self._get_foods('sauce')
        sauces = [food['description'] for food in foods if 'sauce' in food['description'].lower()]
        if not sauces:
            return 'unknown sauce'
        return random.choice(sauces)

    def get_random_cheese(self):
        foods = self._get_foods('cheese')
        cheeses = [food['description'] for food in foods if 'cheese' in food['description'].lower()]
        if not cheeses:
            return 'unknown cheese'
        return random.choice(cheeses)