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

    def __init__(self, msisdn, network, month, product, amount):
        self.msisdn = msisdn
        self.network = network
        self.product = product
        if(self.isMonthValid(month)):
            self.month = month
        if(self.isAmountValid(amount)):
            self.amount = Decimal(amount)

    def display(self, reducer=False):
        if(reducer):
            self.network = repr(self.network.title())
            self.product = repr(self.product.title())
            self.month = repr(self.month.title())
        return(
            '{},{},{},{}'
            .format(
                self.network,
                self.product,
                self.month,
                self.amount
            )
        )

    def getMonth(self):
        return self.month

    def getNetwork(self):
        return self.network

    def getProduct(self):
        return self.product

    def getAmount(self):
        return self.amount

    def updateAmount(self, amount):
        self.amount += amount

    @staticmethod
    def isMonthValid(month):
        ans = False
        months = [
            'Jan',
            'Feb',
            'Mar',
            'Apr',
            'May',
            'Jun',
            'Jul',
            'Aug',
            'Sep',
            'Oct',
            'Nov',
            'Dec'
        ]
        if(month in months):
            ans = True
        else:
            errorMsg = 'Given month is invalid: ' + month
            logging.error(errorMsg)
        return ans

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
