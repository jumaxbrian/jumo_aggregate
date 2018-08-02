import unittest
import datetime

from loan import Loan


class TestLoan(unittest.TestCase):
    def test_get_amount(self):
        tempLoan = Loan(
            1000000,
            'Network 1',
            '12-Mar-2016',
            'Loan Product 1',
            1000.50
        )
        self.assertEqual(tempLoan.getAmount(), 1000.50)

    def test_get_network(self):
        tempLoan = Loan(
            1000000,
            'Network 1',
            '12-Mar-2016',
            'Loan Product 1',
            1000.50
        )
        self.assertEqual(tempLoan.getNetwork(), 'Network 1')

    def test_get_product(self):
        tempLoan = Loan(
            1000000,
            'Network 1',
            '12-Mar-2016',
            'Loan Product 1',
            1000.50
        )
        self.assertEqual(tempLoan.getProduct(), 'Loan Product 1')

    def test_get_month(self):
        tempLoan = Loan(
            1000000,
            'Network 1',
            'Mar',
            'Loan Product 1',
            1000.50
        )
        self.assertEqual(tempLoan.getMonth(), 'Mar')

    def test_update_amount(self):
        tempLoan = Loan(
            1000000,
            'Network 1',
            'Mar',
            'Loan Product 1',
            1000.50
        )
        tempLoan.updateAmount(2000.50)
        self.assertEqual(tempLoan.getAmount(), 3001)

    def test_display(self):
        tempLoan = Loan(
            1000000,
            'Network 1',
            'Mar',
            'Loan Product 1',
            1000.50
        )
        self.assertEqual(
            tempLoan.display(),
            'Network 1,Loan Product 1,Mar,1000.5'
        )

    def test_convert_wrong_string_to_date(self):
        self.assertRaises(
            ValueError,
            Loan.convertStringToDate,
            '12-Mak-2016',
        )

    def tests_convert_right_string_to_date(self):
        date_string = '12-Mar-2016'
        self.assertEqual(
            Loan.convertStringToDate(date_string),
            datetime.datetime.strptime(date_string, '%d-%b-%Y')
        )

    def test_if_date_is_valid(self):
        self.assertTrue(Loan.isDateValid('12-Mar-2016'))
        self.assertFalse(Loan.isDateValid('12-Mak-2016'))

    def test_if_amount_is_valid(self):
        self.assertTrue(Loan.isAmountValid('4000'))
        self.assertFalse(Loan.isAmountValid('45i'))

    def test_extract_month(self):
        self.assertEqual(Loan.extractMonthFromDate('12-Mar-2016'), 'Mar')

    def test_is_month_valid(self):
        self.assertTrue(Loan.isMonthValid('Mar'))
        self.assertFalse(Loan.isMonthValid('may'))


if __name__ == "__main__":
    unittest.main()
