midterm1 = int(input("Midterm1:"))
midterm2 = int(input("Midterm2:"))
final = int(input("Final:"))

grade =  midterm1 * 3/10 + midterm2 * 3/10 + final * 4/10

if (grade >= 90):
    print("AA")
elif (grade >= 85):
    print("BA")
elif (grade >= 80):
    print("BB")
elif (grade >= 75):
    print("CB")
elif (grade >= 70):
    print("CC")
elif (grade >= 65):
    print("DC")
elif (grade >= 60):
    print("DD")
elif (grade >= 55):
    print("FD")
else:
    print("FF")