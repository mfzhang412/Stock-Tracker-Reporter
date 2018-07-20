from Data_Analysis_Interface import Data_Analysis_Interface as DAI

class Company(DAI):
    """This class handles data acquisition, data analysis, and data storage related to a company"""
    ### Instance variables
    # String company_name
    # String stock_symbol
    # String[] urls
    # List[] rel_data
    # String[] exec_names
    # String industry
    # Company[] prev_data
    # String storage_loc
    
    def __init__(self,company_name,stock_symbol,urls,rel_data,exec_names,industry,prev_data,storage_loc):
        """Initialize Companies object"""
        this.company_name = company_name
        this.stock_symbol = stock_symbol
        this.urls = urls
        this.rel_data = rel_data
        this.exec_names = exec_names
        this.industry = industry
        this.prev_data = prev_data
        this.storage_loc = storage_loc

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
