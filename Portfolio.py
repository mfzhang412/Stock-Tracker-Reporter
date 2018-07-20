from Data_Analysis_Interface import Data_Analysis_Interface as DAI

class Portfolio(DAI):
    """This class handles data acquisition, data analysis, and data storage related to a top performing stock portfolio"""
    ### Instance variables
    # String name
    # Company[] companies
    # String website
    # String storage_loc
    # List[] prev_data
    
    def __init__(self,name,companies,website,storage_loc,prev_data):
        """Initialize Portfolios object"""
        this.name = name
        this.companies = companies
        this.website = website
        this.storage_loc = storage_loc
        this.prev_data = prev_data

    def access_urls(self):
        """Access urls and load websites as objects"""
        pass
    
    def grab_data(self,save_file):
        """Scrape website objects for relevant data"""
        pass

    def store_data(self):
        """Store data obtained from initial scraping"""
        pass

    def analyze_data(self):
        """Perform calculations on data obtained from initial scraping to obtain more data"""
        pass

    def store_analysis(self):
        """Store new data with the old data"""
        pass

    def set(self):
        """Set functions: information needed to perform tasks related to scraping, storing, and anlyzing data"""
        pass

    def get(self):
        """Get functions: ways to get the new and old data from save files (as strings/well formatted chunks) so one can populate report with information by calling get functions"""
        pass
