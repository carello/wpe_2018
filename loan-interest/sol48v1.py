#!/usr/bin/env python3

import arrow
from pprint import pprint


class Loan(object):
    def __init__(self, amount, interest_rate, starts_on=None):
        self.amount = amount
        self.interest_rate = interest_rate

        # Default to today, if starts_on isn't otherwise set
        if starts_on is None:
            starts_on = arrow.now().format('YYYY-MM-DD')

        self.starts_on = arrow.get(starts_on)

    def total_on(self, ends_on):
        ends_on = arrow.get(ends_on)
        years = (ends_on - self.starts_on).days / 365
        return self.amount * ((1 + self.interest_rate) ** years)

    def total_on_each(self, range_start, range_end):
        return [(str(one_day.date()), self.total_on(one_day))
                for one_day, _ in arrow.Arrow.span_range('day',
                                                         arrow.get(range_start),
                                                         arrow.get(range_end))]


my_loan = Loan(1000, 0.02)
print(my_loan.amount)
print(my_loan.interest_rate)
print(my_loan.starts_on)
print(my_loan.total_on('2019-03-30'))
print("$$$$$$$$$$$$$$$$$$")
my_loan2 = Loan(2000, 0.05, starts_on='2019-01-01')
print(my_loan2.amount)
print(my_loan2.interest_rate)
print(my_loan2.starts_on)
print("$$$$$$$$$$$$$$$$$$")
pprint(my_loan2.total_on_each('2019-02-01', '2019-02-28'))
