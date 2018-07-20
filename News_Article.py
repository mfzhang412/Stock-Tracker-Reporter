from Data_Analysis_Interface import Data_Analysis_Interface as DAI

class News_Article(DAI):
    """This class handles data acquisition, data analysis, and data storage related to a recent news article"""
    ### Instance variables
    # String website
    # String article_name
    # String rep_agency
    # String[] rel_keywords
    # int num_views
    # String storage_loc
    # List[] prev_data
    
    def __init__(self,data_list):
        """Initialize News object"""
        this.rel_dat = data_list
    
    def scrape_web(self):
        """Access websites from save file and scrape them for relevant data"""
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
