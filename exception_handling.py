# try:
#   age = int(input("Enter your age: "))
#   print(f"You are {age} years old")
# except ValueError:
#   print("Please enter a valid number")

# print("Program continues...")

try:
  num1 = int(input("Enter first number:\n"))
  num2 = int(input("Enter second number:\n"))
  
  result = num1 / num2
  print(f"{num1} / {num2} = {result}")

  result2 = num1 / "abc"

except ZeroDivisionError:
  print("Cannot divide by Zero")
except ValueError:
  print("Please enter valid numbers")
except Exception as e:
  print(f"Something unexpectedly happened: {e}")