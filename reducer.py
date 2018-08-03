#!/usr/bin/env python

import sys
from loan_processor import LoanProcessor
from loan import Loan

loanProcessor = None


def processInput(line):
    network, product, month, amount = line.split(',')
    global loanProcessor
    newLoan = Loan('', network, month, product, amount)
    if loanProcessor is not None:
        loanProcessor.processNewLoan(newLoan, reducer=True)
    else:
        loanProcessor = LoanProcessor(newLoan)


if __name__ == "__main__":
    for line in sys.stdin:
        processInput(line)
    output = loanProcessor.displayCurrentAggregate(reducer=True) + '\n'
    sys.stdout.write(output)
