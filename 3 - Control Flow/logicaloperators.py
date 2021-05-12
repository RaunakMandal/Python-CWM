# Logical operators are short circuits
high_income = False
good_credit = True

# Both will be checked
if high_income and good_credit:  # don't have to write == True as both are booleans
    print("Eligible for loan")
else:
    print("Not Eligible")

# any one has to be true
if high_income or good_credit:  # don't have to write == True as both are booleans
    print("Eligible for loan")
else:
    print("Not Eligible")

# checks one condition only
student = False
if not student:
    print("Eligible for loan")
else:
    print("Not Eligible")

# all in one
if high_income or good_credit and not student:
    print("Eligible")
else:
    print("Not eligible")
