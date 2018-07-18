from bs4 import BeautifulSoup
from Report import Report

class Stock_Tracker:
    '''This class tracks and sends daily reports on specific stocks using web scraping'''
    def __init__(self):
        '''Initialize a Stock_Tracker object'''
        pass

    def create_report(self):
        '''Create a formatted report and save it'''
        pass

    def send_report(self):
        '''Send a saved report at a designated time'''
        pass
    
    def grab_stocks(self):
        '''Grab stocks from the "Stock_Watchlist.txt" watchlist document'''
        pass

    def generate_report(self):
        '''Format data into readable and stylized report'''
        pass

    def send_report(self):
        '''Send the report'''
        pass



def main():
    '''Main function'''
    tracker = Stock_Tracker()
    tracker.create_report()
    tracker.send_report()

if __name__ == "__main__":
    main()
