name = input("Enter employee's name: ")
hrs_worked = float(input("Enter number of hours worked in a week: "))
hourly_pay_rate = float(input("Enter hourly pay rate: "))
federal_tax = float(input("Enter federal tax withholding rate: "))
state_tax = float(input("Enter state tax withholding rate: "))

gross_pay = hrs_worked * hourly_pay_rate
federal_withholding = (federal_tax / 100) * gross_pay
state_withholding = (state_tax / 100) * gross_pay
total_deduction = federal_withholding + state_withholding
net_pay = gross_pay - total_deduction

print()
print(f"{name}\nHours worked: {hrs_worked}\nPay Rate: {hourly_pay_rate}\nGross Pay: {gross_pay}")
print(f"Deduction: \nFederal Withholding: {federal_withholding:.2f}\nState withholding: {state_withholding:.2f} \nTotal Deduction: {total_deduction} \n Net Pay: {net_pay}")