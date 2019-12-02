'''
Interest Calculator program
This program computes the interest accrued over the specified no. of years on the principal amount with one year
as a fixed value for the compound interval.
A = P * (1 + r/n)^(nt)
where:
P = principal amount (initial investment).
r = annual nominal interest rate (as a decimal).
n = number of times the interest is compounded per year.
t = number of years.
'''


print("Interest Calculator:")
amount = float(input("Principal amount ?"))
roi = float(input("Rate of Interest ?"))
years = int(input("Duration (no. of years) ?"))
total = (amount * pow( 1 + (roi / 100), years))
interest = total - amount
print("\nInterest = %0.2f" %interest)
