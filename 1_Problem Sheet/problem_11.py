# Write a program to find the simple interest when the value of principle,rate of interest and time period is given.
# Simple Interest = (P*R*T)/100
# P = Principle
# R = Rate of Interest
# T = Time Period
# P = 1000
# R = 5
# T = 2
# Simple Interest = (1000*5*2)/100 = 100


def cal_simple_interest(p,r,t):
    si = (p*r*t)/100
    return si


principle = int(input("Enter the value of principle:"))
rate_of_interest = int(input("Enter the value of rate of interest:"))
time = int(input("Enter the value of time period:"))
print("Simple Interest is: ",cal_simple_interest(principle, rate_of_interest, time))