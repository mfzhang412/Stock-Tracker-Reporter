from bs4 import BeautifulSoup
from Report import Report

class Stock_Tracker:
    """This class automates tracking specific stocks and sending daily reports"""

    def __init__(self):
        """Initialize a Stock_Tracker object"""
        pass

    def grab_stocks(self):
        """Return stocks recorded in text file document"""
        pass

    def create_report(self):
        """Create a formatted report with relevant information and save it"""
        pass

    def send_report(self):
        """Load and send a saved report at a scheduled time"""
        pass



def main():
    """Main function"""
    tracker = Stock_Tracker()
    tracker.grab_stocks()
    tracker.create_report()
    tracker.send_report()

if __name__ == "__main__":
    main()
