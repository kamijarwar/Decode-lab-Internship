
print ("---------------------------------------Expense Tracker--------------------------------------------")

total = 0

while True :
    expense = float (input ("Enter Expense Amount: "))

    total = total + expense

    choice =  (input ("Add another expense? (y/n): "))

    if choice.lower() == "n" :
       break

print ("\nTotal spent =",total)

print ("Thank You For using Expense Tracker")


Added Expense Tracker task
