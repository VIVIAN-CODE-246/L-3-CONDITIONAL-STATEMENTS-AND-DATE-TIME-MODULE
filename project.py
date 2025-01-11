number = 10
if number > 50:
    print("Yes")
elif number < 50:
    print("No")
else:
    print("Invalid Input")

num = float(input("Enter your age:"))
if num>=0:
    if num > 18:
        print("Adult")
    else:
        print("Underage")
else:
    print("Wrond Input")