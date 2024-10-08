# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
fixed_payment = 2684.11
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

total_paid = 0.0
months = 0

while principal > 0:
    months += 1
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        payment = fixed_payment + extra_payment
    else:
        payment = fixed_payment

    if payment > principal:
        payment = principal * (1 + rate / 12)

    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    print(f"{months} {round(total_paid, 2)} {round(principal, 2)}")

print("Total paid", round(total_paid, 2))
print("Months", months)
