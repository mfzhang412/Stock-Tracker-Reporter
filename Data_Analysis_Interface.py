from abc import ABC, abstractmethod

class Data_Analysis_Interface(ABC):
    '''This is an interface for the acquisition, analysis, and storage of data'''

    @abstractmethod
    def scrape_web(self):
        '''Scrape web'''
        pass

    @abstractmethod
    def store_data(self):
        '''Store data'''
        pass

    @abstractmethod
    def analyze_data(self):
        '''Analyze data'''
        pass

    @abstractmethod
    def store_analysis(self):
        '''Store analyzed data'''
        pass
