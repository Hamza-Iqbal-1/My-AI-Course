# Question no 01
'''Write a program that converts a temperature from Celsius to Fahrenheit. (Formula: Fahrenheit = 
(Celsius * 9/5) + 32) '''

a = float(input("Enter temperature in Celsius: "))
f = (a * 9/5) + 32  
print("The temperature in Fahrenheit is: " + str(f) + "°F")

# Question no 02
'''Calculate Area of a Rectangle '''

L = float(input("Enter the length of the rectangle: "))
W = float(input("Enter the width of the rectangle: "))
area = L * W
print("The area of the rectangle is: " + str(area) + " square units")

# Question no 03
''' Calculate Compound Interest 
Use the formula: 
CI = P * (1 + R/100)**T - P 
Where P = principal, R = rate, T = time '''

p = float(input("Enter the principal amount: "))
R = float(input("Enter the principal amount: "))
T = float(input("Enter the principal amount: "))
CI = p * (1 + R/100)**T - p
short_CI = round(CI, 2)
print("Compound interest is: " + str(short_CI))

# Question no 04
''' Perimeter of a Rectangle - Take length and width as input and calculate the perimeter '''

L = float(input("Enter the length of the rectangle in meter: "))
W = float(input("Enter the width of the rectangle in meter : "))
perimeter = 2 * (L + W)        # formula of perimeter of length
print("The perimeter of rectangle  is: " + str(perimeter) + " m")

# Question no 05
''' Average of Three Numbers - Input three numbers and print their average '''

no1 = float(input("Enter number 01: "))
no2 = float(input("Enter number 02: "))
no3 = float(input("Enter number 03: "))
average = (no1 + no2 + no3) / 3
print("Average of three numbers is: " + str(average))

# Question no 06
''' Square and Cube of a Number - Ask the user for a number and display its square and cube '''

a = float(input("Enter the number: "))
sq = a ** 2
cube = a ** 3
print(f"Square of number is {sq} and cube of number is {cube}")

# Question no 07
''' Distribute Items Equally - You have n candies and k students. 
Write a program to find: 
how many candies each student gets 
how many are left '''

n = int(input(" Enter number of candies: "))
k = int(input(" Enter number of students: "))
each_get = n // k
left_over = n % k
print(f"Each student get {each_get} candies and remaining candies are {left_over}")

# Question no 08
''' Calculate Profit or Loss 
Input cost price and selling price.
Display either: Profit and amount, 
or Loss and amount, 
or No Profit No Loss '''

cost = float(input("Enter cost price: "))
sell = float(input("Enter selling price: "))
if sell > cost:
    profit = sell - cost
    print(f"Profit amount is: {profit}")
elif sell < cost:
    loss = cost - sell 
    print(f"Loss amount is: {loss}")
else:
    print("No profit no loss")
    
# Question no 09
''' Total Marks and Percentage 
Input marks of 5 subjects. Print: 
 Total marks 
 Percentage 
 Average '''

sub1 = float(input("Enter obtaining marks of subject 01 out of 100: "))
sub2 = float(input("Enter obtaining marks of subject 02 out of 100: "))
sub3 = float(input("Enter obtaining marks of subject 03 out of 100: "))
sub4 = float(input("Enter obtaining marks of subject 04 out of 100: "))
sub5 = float(input("Enter obtaining marks of subject 05 out of 100: "))
total = sub1 + sub2 + sub3 + sub4 + sub5
per = (total/500) * 100
ave = total / 5
print(f"Total obtaining marks are: {total}")
print(f"Percentage is: {per} %")
print(f"Average is: {ave}")

# Question no 10
''' Salary Calculator 
Input basic salary. Calculate: 
 HRA = 20% of basic 
 DA = 15% of basic 
 Total Salary = Basic + HRA + DA '''

bs = int(input("Enter basic salary: "))
hra = (bs * 20) / 100
da = (bs * 15) / 100
total = bs + hra + da 
print("Total salary after adding HRA and DA is: ", int(total))

# Question no 11
''' Age in Months and Days 
Input your age in years. Calculate and print age in: 
 Months 
 Days (approximate) '''

age = int(input("Enter age in years: "))
month = age * 12
days = age * 365
print("Age in month: ", month, "months")
print("Age in days: ", days, "days")

# Question no 12
''' Currency Converter (USD to PKR) 
Input amount in USD. Convert using a fixed exchange rate '''

amount = float(input("Enter amount in USD: "))
after_exchange = (amount * 284.38)    # 284.38 is fixed price for 1 USD
print("Amount in PKR is: ", after_exchange,"PKR")

# Question no 13
''' Sum of First N Natural Numbers 
Input a number n, calculate sum of first n natural numbers. 
Formula: sum = n * (n + 1) / 2 '''

n = int(input("Enter number: "))
sum = int(n * (n + 1) / 2)
print("Sum of first N natural number is: ", sum)

# Question no 14
''' Percentage of Correct Answers 
Input total questions and correct answers, and calculate the percentage score '''

total = int(input("Enter total number of questions: "))
correct = int(input("Enter number of correct answers: "))
percentage = (correct / total) * 100
print(f"percentage score is: {percentage}%")

# Question no 15
''' Speed, Distance, and Time 
Input distance and time, and calculate speed. '''

distance = float(input("Enter distance in meters: "))
time = float(input("Enter time in hours: "))
speed = distance / time
print("Speed is: ", speed, "m/h")

# Question no 16
''' Calculate Body Mass Index (BMI) 
Input weight (kg) and height (m), then calculate: 
BMI = weight / (height ** 2) '''

weight = float(input("Enter weight in Kg: "))
height = float(input("Enter height in m: "))
bmi = weight / (height ** 2)
print("Body Mass Index(BMI) is: ", round(bmi,2))

# Question no 17
''' Convert Minutes to Hours and Minutes 
Input number of minutes and convert to hours and remaining minutes. 
Example: 130 minutes → 2 hours 10 minutes '''

minutes = int(input("Enter number of minutes: "))
hours = minutes // 60
rem_min = minutes % 60
print("After converting into hours and minutes: ", minutes, "minutes = ", hours, "hours ", rem_min, "minutes")