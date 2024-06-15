#Date: 14/6/2024
#Author: Muhammad Muzammil

#Calculate the compound interest for a given principal amount, interest rate, and time period. 
'''
Formula= A = P (1 + R/N) ^ nt

Where:

A is the final amount
P is the principal amount
r is the annual interest rate (decimal)
n is the number of times interest is compounded per year (12 for monthly)
t is the time in years
'''

def compound_interest(p_amount, rate, n_months, t_years):

    final_amount =  p_amount * ((1 + rate/n_months) **  (n_months*t_years))
    
    compound_interest =  final_amount - p_amount
    return compound_interest

print(compound_interest(1000, 0.06, 12, 3))
#2000 amount, 6% interest rate, monthly, 3 years


#You can also use the built-in power function
#final_amount = p_amount * (pow((1 + r_rate/n_months),  (n_months*t_years)))


