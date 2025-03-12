total = 0

while True:

    number = input("Number: ")

    if (number == "q"):
        break
    number = int(number)

    total += number

print("Total number is : ", total)