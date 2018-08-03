import datetime
import logging
from decimal import Decimal

# Setup for logging
logging.basicConfig(
    filename='app.log',
    format='%(asctime)s:%(levelname)s:%(message)s'
)


class Loan:
    '''
    Loan represents a single loan transaction i.e. line in Loans.csv
    '''

    def __init__(self, msisd, network, month_year, product, amount):
        self.msisd = msisd
        self.network = network
        self.product = product
        self.month_year = month_year  # rep month-year
        if(self.isAmountValid(amount)):
            self.amount = Decimal(amount)

    def display(self, reducer=False):
        if(reducer):
            self.network = repr(self.network.title())
            self.product = repr(self.product.title())
            self.month_year = repr(self.month_year.title())
        return(
            '{},{},{},{}'
            .format(
                self.network,
                self.product,
                self.month_year,
                self.amount
            )
        )

    def getMonthYear(self):
        return self.month_year

    def getNetwork(self):
        return self.network

    def getProduct(self):
        return self.product

    def getAmount(self):
        return self.amount

    def updateAmount(self, amount):
        self.amount += amount

    @staticmethod
    def isDateValid(date_string):
        ans = False
        try:
            Loan.convertStringToDate(date_string)
            ans = True
        except:
            errorMsg = 'Date string not a valid date: ' + date_string
            logging.error(errorMsg)
        return ans

    @staticmethod
    def extractMonthFromDate(date_string):
        return Loan.convertStringToDate(date_string).strftime('%b')

    @staticmethod
    def extractMonthYearFromDate(date_string):
        return Loan.convertStringToDate(date_string).strftime('%b-%Y')

    @staticmethod
    def isAmountValid(amountStr):
        ans = False
        try:
            amountDecimal = Decimal(amountStr)
            ans = True
        except:
            errorMsg = 'Amounts should only contain digits 0-9 and a decimal point: ' + amountStr
            logging.error(errorMsg)
        return ans

    @staticmethod
    def convertStringToDate(date_string):
        return datetime.datetime.strptime(date_string, '%d-%b-%Y')
