number = 11

if number %2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

print(24 %5)

#BMI: Body Mass Index
height = 2.5
weight = 80


bmi = weight / height * height
if bmi <= 18.4:
    print("You are underweight")
elif bmi <= 24.9:
    print("You are healthy")
elif bmi <= 29.9:
    print("You are overweight")
elif bmi <= 34.9:
    print("You are severely overweight")
elif bmi <= 39.9:
    print("You are obese")
else:
    print("You are severely obese")

#date time
import datetime
print(datetime.datetime.now())
import calendar
print(calendar.calendar(1))