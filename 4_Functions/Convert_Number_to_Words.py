# Lists for digits and tens
ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]


# Function to convert number to words
def number_to_words(number):
    first_digit = number % 10  # Ones place
    second_digit = number // 10  # Tens place

    return tens[second_digit] + " " + ones[first_digit]


# User input
number = int(input("Enter a number: "))

# Print the result
print(number_to_words(number))
