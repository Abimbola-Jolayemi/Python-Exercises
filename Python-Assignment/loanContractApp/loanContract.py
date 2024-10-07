class LoanContract:

    def __init__(self, name_of_borrower, interest_rate, loan_amount, loan_period):
        self._name_of_borrower = name_of_borrower
        self._interest_rate = self._validate_interest_rate(interest_rate)
        self._loan_amount = self._validate_loan_amount(loan_amount)
        self._loan_period = self._validate_loan_period(loan_period)

    def get_name_of_borrower(self):
        return self._name_of_borrower

    def _validate_interest_rate(self, interest_rate):
        if interest_rate <= 0:
            raise ValueError("Interest rate must be greater than 0.")
        return interest_rate

    def _validate_loan_amount(self, loan_amount):
        if loan_amount <= 0:
            raise ValueError("Loan amount must be greater than 0.")
        return loan_amount

    def _validate_loan_period(self, loan_period):
        if loan_period <= 0:
            raise ValueError("Loan period must be greater than 0.")
        return loan_period

    def compute_monthly_payment(self):
        annual_interest_rate = self._interest_rate / 100
        monthly_interest_rate = annual_interest_rate / 12
        duration_in_months = self._loan_period * 12
        numerator = self._loan_amount * monthly_interest_rate
        denominator = 1 - (1 / (1 + monthly_interest_rate)) ** duration_in_months
        return numerator / denominator

    def compute_total_payment(self):
        return self.compute_monthly_payment() + (self._loan_period * 12)

