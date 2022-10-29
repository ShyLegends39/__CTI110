# Brief Description: This program work on some employee info and salary,
#  that processes the salary and info then displays it!

# CTI-110

# P3HW2 - Salary

# Kelly Bullard

# October 26, 2022

#

# In Python
# This program's inputs are: emplName, hoursWork(use float with this), payRate(use float with this) & that ask 'Enter ...' with its assign input.
# Do calculate & this process the inputs (except the name that can go to output): if-else for overtime, and do a calculation for overTime and the others
# (hoursWork, payRate, overTimePay, regHrsPay, grossPay), if not then just calculate regHrsPay & grossPay use the else part of the if-else.
# For the output, you need a line of - (just long that pass name output by inch left) and after that have an output for epmlName(name)with 'Employee's name: ',
# and then use print('') after emplName's output for a space to seperate the next part.
# Next in the output, you have these labels (Hours Worked, Pay Rate, OverTime, OverTime Pay, RegHour Pay, Gross Pay)/w spacing
# for hoursWork, payRate, overTime, overTimePay, regHrsPay, grossPay, and then another line of - (but longer), and then the output (w/ float)
# for hoursWork, payRate, overTime, overTimePay, regHrsPay, grossPay w/ the first three having .1f and the last three having .2f
# w/ the last two having $ before this {
# and lastly with each one .1f or .2f and before that have: <15(w/ first one and the last two), <13(w/ second one and the third one),
# <18(w/ the fourth one), but after the :. So, the they are aline with their labels.


# Input
emplName = input("Enter employee's name: ")
hoursWork = float(input('Enter number of hours worked: '))
payRate = float(input("Enter employee's pay rate: "))

# Calculate and process
if hoursWork > 40:
 overTime = hoursWork - 40
 overTimePay = overTime * payRate * 1.5
 regHrsPay = 40 * payRate
 grossPay = regHrsPay + overTimePay

else:
 regHrsPay = hoursWork * payRate
 grossPay = regHrsPay


# Output
print('---------------------------------------')
print('Employee name:  ', emplName)
print('') # Space
print('Hours Worked   Pay Rate     OverTime     OverTime Pay      RegHour Pay     Gross Pay       ')
print('-----------------------------------------------------------------------------------------------')
print(f'{hoursWork:<15.1f}{payRate:<13.1f}{overTime:<13.1f}{overTimePay:<18.2f}${regHrsPay:<15.2f}${grossPay:<15.2f}')
