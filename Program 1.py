x = int(input("Enter the Number of Years: "))
i = x*12
z = 0
c=0
while i >= x:
          for a in range(1, 13):
                 i=i-1
                 y =int(input(f"Enter Your month {a} Highest Temperature: "))
                 if (y>c):
                   z=z+y
                   b=z/y
                   c=y

print("Total",z) 
print("Average",b)
print("Highest Temperature",c)