import requests
import os
from ..base import BaseELTJob

class OpenWeatherExtractor(BaseELTJob):
    def __init__(self, city):
        super().__init__(city)

        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.url="https://api.openweathermap.org/data/2.5/forecast"
        self.params = {'q': self.city, 'appid': self.api_key}

    def get_name(self):
        return "OpenWeatherMap"
    
    def fetch_data(self):
        response = requests.get(self.url, params = self.params)

        response.raise_for_status()
        return response.json()
        