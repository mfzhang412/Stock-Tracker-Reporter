from bs4 import BeautifulSoup
from Report import Report

class Stock_Tracker:
    """This class automates tracking specific stocks and sending daily reports"""
    ### Instance variables
    # List[] stock_list
    # Report report

    def __init__(self,file_loc='default'):
        """Initialize a Stock_Tracker object"""
        # gets the stocks currently in the file
        this.stock_list = this.grab_stocks(file_loc)
        this.report = None

    def grab_stocks(self,file_name='default'):
        """Return stocks recorded in text file document"""
        # open watchlist text document in read mode
        file = open(file_name,'r')
        # read and store contents into a list
        stocks = []
        if file.mode == 'r':
            lines = file.readlines()
            for i in range(len(lines)):
                temp = lines[i].split('\n')
                if ('\n' in temp): del temp[temp.index('\n')]
                stocks.append(temp)
        else:
            print("File not found")
        # close watchlist text document
        file.close()
        # return list
        return stocks

    def create_report(self,template='default',save_loc='default'):
        """Create a formatted report with relevant information and save it"""
        # create Report object with relevant company, portfolio, and news data
        rep = Report()
        #####report.gather_data_chunks()    should be part of Report __init__
        # populate report in the format of a chosen template
        rep.build_report(template)
        this.report = rep.get_report()
        # save report in specified location
        save_log = rep.save_report(save_loc)
        # return the log of the saved report
        return save_log

    def send_report(self,report_loc,time='default',comm_option='default'):
        """Load and send a saved report at a scheduled time"""
        # load report from location
        rep = load_report(report_loc)
        # wait until scheduled time
        rep.wait_function(time)
        # send report through the option chosen
        send_log = rep.issue_report(comm_option)
        # return the log of the sent report
        return send_log

    def get_report(self):
        """Return report attribute"""
        return this.report




def main():
    """Main function"""
    # create Stock_Tracker object with a list containing companies and their stock symbols
    tracker = Stock_Tracker("<watchlist file path>")
    # create a report formatted based on a chosen template
    create_log = tracker.create_report("<template choice>","<save location>")
    # send a report at a specified time with a chosen communication method
    send_log = tracker.send_report("<report to be sent loation>","<scheduled time>","<communication method>")
    if send_log != "": print("Report succesfully sent")
    else: print("Report unsuccessfully sent")

if __name__ == "__main__":
    main()
