# day_of_week = input("Enter the Day of Week:")
# print(day_of_week.lower())

# day_of_week = input("Enter the Day of Week:").lower()
# print(day_of_week)

# if day_of_week == "sunday" or day_of_week == "saturday": ##TRUE -- this is fine and correct
# ## if day_of_week == "Sunday" or "sunday" or day_of_week == "saturday" or "saturday": ##TRUE -- this is also fine and correct
# ## if day_of_week == "Sunday".lower() or day_of_week == "Saturday".lower(): ##TRUE -- this is also fine and correct
#     print("I will LEARN LIVE PYTHON FOR DEVOPS")
# else: ##FALSE
#     print("I will Practice PYTHON")


## 2 ##
number1 = int(input("Enter the First Number:"))
number2 = int(input("Enter the Second Number:"))

choice = input("Enter your choice: (Operations: +, -, *, /, %): ")

if choice == "+":
    sum_of_numbers = number1 + number2
    print("Addition of two numbers:", sum_of_numbers)
    ## print("addition of two numbers:", number1 + number2)

elif choice == "-":
    diff_of_numbers = number1 - number2
    print("Diff of two numbers:", diff_of_numbers)
elif choice == "*":
    product_of_numbers = number1 * number2
    print("Product of two numbers:", product_of_numbers)
elif choice == "/":
    division_of_numbers = number1 / number2
    print("Division of two numbers:", division_of_numbers)
elif choice == "%":
    mod_of_numbers = number1 % number2
    print("Modulus of two numbers:", mod_of_numbers)
else:
    print("Oops! Invalid Choice, Please try to choose valid choice between +, -, *, /, %")