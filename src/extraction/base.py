from abc import ABC, abstractmethod

class BaseELTJob(ABC):
    def __init__(self, city):
        self.city = city
    

    @abstractmethod
    def fetch_data(self):
        pass

    @abstractmethod
    def get_name(self):
        pass
