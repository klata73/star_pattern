a = int(input("How many rows u want\n"))
b = bool(int(input("Type 0 or 1\n")))

if b == True:
    count = 0
    while(count<=a):
        print("*" * count, end = "\n")
        count = count +1
else:
     count = a
     while(count!= 0):
            print("*" * count, end = "\n")
            count = count- 1

