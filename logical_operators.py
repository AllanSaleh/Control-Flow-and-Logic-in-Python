is_sunny = True
is_warm = True
has_time = False

# AND: All condition must be true
if is_sunny and is_warm:
  print("Perfect beach day!")

if is_sunny and is_warm and has_time:
  print("Let's go to the beach now!")
else:
  print("Maybe another time")


# OR: At least one condition must be true
is_raining = True
is_cold = True
is_Tired = False

if is_raining or is_cold:
  print("Stay inside!")

if(is_raining or is_cold or is_Tired):
  print("Good day to stay at home!")


# NOT: it reverses the truth of something
# True => False, False => True

is_weekend = False
is_busy = False

# Checking to see if is_weekend is false
# is_weekend == False
if not is_weekend:
  print("It's a weekday")

if not is_busy:
  print("Free to hang out!")


# Truth Tables
print("Truth Table for AND")
print(f"True and True = {True and True}")
print(f"True and False = {True and False}")
print(f"False and True = {False and True}")
print(f"False and False = {False and False}")

print("Truth Table for OR")
print(f"True or True = {True or True}")
print(f"True or False = {True or False}")
print(f"False or True = {False or True}")
print(f"False or False = {False or False}")


is_snowing = True

if not is_snowing:
  print("You don't need an umbrella")
else:
  print("You do need an umbrella")


print(not True)
print(not False)