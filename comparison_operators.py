num1 = 5
num2 = 10

# Numerical Comparisons
print(f"{num1} == {num2} is {num1 == num2}")

# not equal !=
print(f"{num1} != {num2} is {num1 != num2}")

print(f"{num1} < {num2} is {num1 < num2}")

print(f"{num1} > {num2} is {num1 > num2}")

# <= less than or equal
print(f"{num1} <= {num2} is {num1 <= num2}")

# >= larger than or equal
print(f"{num1} >= {num2} is {num1 >= num2}")



name1 = "Alice"
name2 = "Bob"
# String Comparisons
print(f"{name1} is {name1 == name2}") # False
print(f"{name1} is {name1 < name2}") #True




# age = 25
# voting_age = 18

# print("Can this person vote?")
# print(f"Age: {age}, Voting age: {voting_age}")

# if(age >= voting_age):
#   print("This person can vote")
# else:
#   print("This person cannot vote")




age2 = 18

if age2 >=18:
  print("you can vote")
  print("This will not alway print")



person_age = 75

# Multiple checks
if person_age < 13:
  print("Child ticket: $5")
  # if the persons age is between 13 and 65
elif person_age >= 13 and person_age < 65:
  print("Adult ticket: $12")
else:
  print("Senior ticket: $8")



