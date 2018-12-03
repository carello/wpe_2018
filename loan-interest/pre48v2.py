import arrow
from decimal import Decimal
from pprint import pprint


class Loan(object):
    def __init__(self, amount, interest, starts_on=None):
        self.amount = Decimal(str(amount))
        self.interest = Decimal(str(interest))
        self.daily_interest = self.interest * self.amount / 365

        if starts_on is None:
            self.starts_on = arrow.now().floor('day')
        else:
            self.starts_on = arrow.get(starts_on, "YYYY-MM-DD")

    def total_on(self, ends_on):
        days = (arrow.get(ends_on, "YYYY-MM-DD") - self.starts_on).days
        print("DAYS: {}".format(days))
        return (0.0 if days < 0 else
                float(round(self.daily_interest * days + self.amount, 2)))

    def total_on_each(self, starts_on, ends_on):
        starts_on = arrow.get(starts_on, 'YYYY-MM-DD')
        ends_on = arrow.get(ends_on, 'YYYY-MM-DD')
        days = (starts_on - self.starts_on).days
        period = (ends_on - starts_on).days
        return [(starts_on.shift(days=i).format(fmt='D MMM YYYY'),
                 0.0 if days + i < 0 else
                 float(round(self.daily_interest * (days + i) + self.amount, 2)))
                for i in range(period + 1)]


my_loan = Loan(1000, 0.02)
print(my_loan.amount)
print(my_loan.interest)
print(my_loan.daily_interest)
print(my_loan.starts_on)
print(my_loan.total_on('2019-03-30'))
print("$$$$$$$$$$$$$$$$$$")
my_loan2 = Loan(2000, 0.05, starts_on='2019-01-01')
print(my_loan2.amount)
print(my_loan2.interest)
print(my_loan2.daily_interest)
print(my_loan2.starts_on)
print("$$$$$$$$$$$$$$$$$$")
pprint(my_loan2.total_on_each('2019-02-01', '2019-02-28'))
