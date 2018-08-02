import datetime
import logging

# Setup for logging
logging.basicConfig(
    filename='app.log',
    format='%(asctime)s:%(levelname)s:%(message)s'
)


class Loan:
    '''
    Loan represents a single loan transaction i.e. line in Loans.csv
    '''

    def __init__(self, msisdn, network, loan_date, product, amount):
        self.msisdn = msisdn
        self.network = network
        self.loan_date = Loan.convertStringToDate(loan_date)
        self.product = product
        self.amount = amount

    def display(self):
        return(
            '{},{},{},{}'
            .format(
                self.network,
                self.product,
                self.getMonth(),
                self.amount
            )
        )

    def getMonth(self):
        return self.loan_date.strftime('%b')

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
    def isAmountValid(amount):
        amountStr = str(amount)
        ans = False
        if any(char not in '0123456789.' for char in amountStr):
            errorMsg = 'Amounts should only contain digits 0-9 and a decimal point: ' + amountStr
            logging.error(errorMsg)
        else:
            ans = True
        return ans

    @staticmethod
    def convertStringToDate(date_string):
        return datetime.datetime.strptime(date_string, '%d-%b-%Y')
