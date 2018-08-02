#!/usr/bin/env python

import sys
from loan_processor import LoanProcessor
from loan import Loan

loanProcessor = None


def processInput(line):
    network, product, month, amount = line.split(',')
    # msisdn = msisdn.strip("'")
    # network = network.strip("'").strip().lower()
    # loan_date = loan_date.strip("'")
    # product = product.strip("'").strip().lower()
    # amount = amount.strip("'")
    global loanProcessor
    newLoan = Loan('', network, month, product, amount)
    if loanProcessor is not None:
        loanProcessor.processNewLoan(newLoan)
    else:
        loanProcessor = LoanProcessor(newLoan)


if __name__ == "__main__":
    for line in sys.stdin:
        processInput(line)
