temperature = int(input("What's the temperature in Celsius? "))

if (temperature <= 0):
  print("Wear a heavy coat")
elif (temperature > 0 and temperature <= 10):
  print("Wear a warm jacket")
elif (11 <= temperature <= 20):
  print("A light jacket is fine")
elif(temperature >20):
  print("T-shirt weather!")



  # Set the correct credentials
correct_username = "admin"
correct_password = "secret123"

# Get user input
username = input("Enter username: ")
password = input("Enter password: ")

if(correct_password == password and correct_username == username):
  print("Welcome!")
elif(correct_password != password and correct_username == username):
  print("Incorrect password")
elif(correct_password == password and correct_username != username):
  print("Username not found")
else:
  print("Invalid credentials")