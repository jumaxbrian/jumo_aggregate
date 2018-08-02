import unittest
import datetime

from loan import Loan

class TestLoan(unittest.TestCase):
    def test_get_month(self):
        tempLoan = Loan(1000000, 'Network 1', '12-Mar-2016', 'Loan Product 1', 1000.50)
        self.assertEqual(tempLoan.getMonth(), 'Mar')

    def test_convert_wrong_string_to_date(self):
        self.assertRaises(ValueError, Loan, 1000000, 'Network 1', '12-Mak-2016', 'Loan Product 1', 1000.50)
    
    def tests_convert_right_string_to_date(self):
        date_string = '12-Mar-2016'
        self.assertEqual(Loan.convertStringToDate(date_string), datetime.datetime.strptime(date_string, '%d-%b-%Y'))

    def test_if_date_is_valid(self):
        self.assertTrue(Loan.isDateValid('12-Mar-2016'))
        self.assertFalse(Loan.isDateValid('12-Mak-2016'))

    def test_if_amount_is_valid(self):
        self.assertTrue(Loan.isAmountValid(4000))
        self.assertFalse(Loan.isAmountValid('45i'))

if __name__ == "__main__":
    unittest.main()
