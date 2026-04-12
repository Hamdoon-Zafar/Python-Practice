cups = input ("\nEnter the number of cups of Coffee you want: ")
price= input("Enter the price for each cup: ")
cups = int(cups)
price = float(price)
total = cups * price
print("\nTotal: ",total)
if(cups<5):
    print("Discount: 0%")
    print("Total after discount: ", total)
if(cups>=5) & (cups <10):
    discount = total * 5/100
    print("Discount: 10%")
    print("Total after discount", discount)
if(cups>= 10):
    discount = total *20/100 
    print("Discount: 20%")
    print("Total after discount: ",discount)
print("---------------------")

# cups and price is taken as input from the user and then the total is displayed 
# the number of cups are then again checked and the discount is applied after that

#QUESTION 2

hours = int(input("\n\n\nEnter total hours your car was parked for: "))
cost = 50 
if hours == 1:
    print("Cost:", cost)
elif hours<11:
    # For each extra hour after the first, add 30
    for i in range(1, hours):
        cost += 30

    print("Cost:", cost)
else:
    for i in range(1, hours):
        cost += 30
    cost += 200
    print("Cost:", cost)

# initialize the cost variable to 50 then if its the first hour 
# 50 is charged then 30 for every other hour and 200 if the hours are more than 10 as a fine

# QUESTION 3
totalSalary = 0
salary = 0
for i in range (1,8):
    hours = int(input(f"\n\n\nEnter the number of hours worked on day {i}: "))
    if hours <=8:
        salary = 1000
        totalSalary += salary
        print("Salary for day ", i,":", salary)
    elif hours > 8:
        extra = (hours - 8)*200
        salary = 1000  + extra
        totalSalary+=salary
        print("Salary for day ", i,":", salary)
print("\nTotal Salary: ", totalSalary)
        
# the number of hours worked is taken from the user and then checked whether there is 
# an overtime or not then the total is displayed
   



