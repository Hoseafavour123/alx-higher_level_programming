#!/usr/bin/python3
roman_to_int = __import__('12-roman_to_int').roman_to_int

print()
print("""Convert Roman Numerals to Integers. Enter q to quit """)
print()

roman_number = str(input("Input Numeral: "))

while roman_number != "Q" or roman_number != "q":
    if roman_number == "q" or roman_number == "Q":
        print("Ended")
        break

    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
    roman_number = str(input("Input Numeral: "))

print()
