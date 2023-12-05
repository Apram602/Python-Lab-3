a = 0
b = 0
c = 0

while True:
    a = float(input("Enter starting daily calorie intake: "))
    b = float(input("Enter average daily percentage decrease: "))
    c = int(input("Enter the number of days: "))

    if a > 0 and b >= 0 and c > 0:
        break
    else:
        print("Please enter positive values.")

x = 1

if b >= 0 or b == 0:
    while x <= c:
        if a > 1200:
            print(f"Day {x}: {a} calories")
            a -= (a * (b / 100))
            x += 1
        else:
            print("The diet has stabilized below 1200 calories.")
            break
