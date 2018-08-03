#!/usr/bin/env python

import sys
from loan import Loan


def processInput(line):
    msisdn, network, loan_date, product, amount = line.split(',')
    msisdn = msisdn.strip("'")
    network = network.strip("'").strip().lower()
    loan_date = loan_date.strip("'")
    product = product.strip("'").strip().lower()
    amount = amount.strip("'")
    if(Loan.isAmountValid(amount) and Loan.isDateValid(loan_date)):
        month = Loan.extractMonthFromDate(loan_date)
        tempLoan = Loan(msisdn, network, month, product, amount)
        sys.stdout.write(tempLoan.display() + '\n')


if __name__ == "__main__":
    for line in sys.stdin:
        processInput(line)
