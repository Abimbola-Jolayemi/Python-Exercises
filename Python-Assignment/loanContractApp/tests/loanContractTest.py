import unittest

import loanContract


class MyTestCase(unittest.TestCase):

        def test_loan_contract_has_name_of_borrower(self):
            loan = loanContract.LoanContract("name of borrower", 12, 5000, 3)
            self.assertEqual(loan.get_name_of_borrower(), "name of borrower")

        def test_loan_contract_cannot_take_a_negative_interest_rate(self):
            with self.assertRaises(ValueError):
                loan = loanContract.LoanContract("name of borrower", -12, 5000, 3)

        def test_loan_contract_cannot_take_a_negative_loan_amount(self):
            with self.assertRaises(ValueError):
                loan = loanContract.LoanContract("name of borrower", 12, -5000, 3)

        def test_loan_contract_cannot_take_a_negative_loan_period(self):
            with self.assertRaises(ValueError):
                loan = loanContract.LoanContract("name of borrower", 12, 5000, -3)

        def test_loan_contract_can_compute_monthly_payment(self):
            loan = loanContract.LoanContract("name of borrower", 12, 5000, 3)

        def test_that_loan_contract_app_can_compute_monthly_payment(self):
            loan = loanContract.LoanContract("name of borrower", 12, 100_000, 3)
            self.assertEqual(loan.compute_monthly_payment(), 3321.4309812851166)

        def test_that_loan_contract_app_can_compute_total_payment(self):
            loan = loanContract.LoanContract("name of borrower", 12, 100_000, 3)
            self.assertEqual(loan.compute_monthly_payment(), 3321.4309812851166)
            self.assertEqual(loan.compute_total_payment(), 3357.4309812851166)


if __name__ == '__main__':
    unittest.main()
