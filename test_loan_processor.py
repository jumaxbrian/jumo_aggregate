import unittest
import datetime

from loan import Loan
from loan_processor import LoanProcessor


class TestLoan(unittest.TestCase):
    def test_if_loan_can_be_aggregated(self):
        tempLoan = Loan(
            1000000,
            'Network 1',
            'Mar',
            'Loan Product 1',
            1000.50,
        )
        loanProcessor = LoanProcessor(tempLoan)
        tempLoan = Loan(
            1000000,
            'Network 1',
            'Mar',
            'Loan Product 1',
            1000.50,
        )
        self.assertTrue(loanProcessor.canBeAggregated(tempLoan))
        tempLoanWithDifferentNetwork = Loan(
            1000000,
            'Network 2',
            'Mar',
            'Loan Product 1',
            1000.50,
        )
        self.assertFalse(
            loanProcessor.canBeAggregated(tempLoanWithDifferentNetwork)
        )
        tempLoanWithDifferentProduct = Loan(
            1000000,
            'Network 1',
            'Mar',
            'Loan Product 2',
            1000.50,
        )
        self.assertFalse(
            loanProcessor.canBeAggregated(tempLoanWithDifferentProduct)
        )
        tempLoanWithDifferentMonth = Loan(
            1000000,
            'Network 1',
            'Apr',
            'Loan Product 1',
            1000.50,
        )
        self.assertFalse(
            loanProcessor.canBeAggregated(tempLoanWithDifferentMonth)
        )

    def test_loan_aggregation(self):
        tempLoan = Loan(
            1000000,
            'Network 1',
            'Mar',
            'Loan Product 1',
            1000.50,
        )
        loanProcessor = LoanProcessor(tempLoan)
        newLoan = Loan(
            1000000,
            'Network 1',
            'Mar',
            'Loan Product 1',
            2000.50,
        )
        loanProcessor.aggregate(newLoan)
        self.assertEqual(3001, loanProcessor.getAggregateAmount())

    def test_new_loan(self):
        tempLoan = Loan(
            1000000,
            'Network 1',
            'Mar',
            'Loan Product 1',
            1000.50,
        )
        loanProcessor = LoanProcessor(tempLoan)
        newLoan = Loan(
            1000001,
            'Network 1',
            'Mar',
            'Loan Product 1',
            2000.50,
        )
        loanProcessor.processNewLoan(newLoan)
        self.assertEqual(3001, loanProcessor.getAggregateAmount())
        newLoan = Loan(
            1000002,
            'Network 3',
            'Mar',
            'Loan Product 1',
            2000.50,
        )
        loanProcessor.processNewLoan(newLoan)
        self.assertEqual(2000.50, loanProcessor.getAggregateAmount())


if __name__ == "__main__":
    unittest.main()
