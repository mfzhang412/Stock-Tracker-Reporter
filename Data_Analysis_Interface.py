from abc import ABC
from abc import abstractmethod

class Data_Analysis_Interface(ABC):
    """This is an interface for the acquisition, analysis, and storage of data"""

    @abstractmethod
    def access_urls(self):
        """Access urls"""
        pass

    @abstractmethod
    def grab_data(self):
        """Scrape websites for data"""
        pass

    @abstractmethod
    def store_data(self):
        """Store data from initial scraping"""
        pass

    @abstractmethod
    def analyze_data(self):
        """Perform calculations on initial scrape data"""
        pass

    @abstractmethod
    def store_analysis(self):
        """Store calculated data"""
        pass
