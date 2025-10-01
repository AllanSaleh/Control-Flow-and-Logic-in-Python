# Lesson 2: Control Flow and Logic - In-Class Practice

## Practice 1: Temperature Advisor (10 minutes)

### 🎯 **Objective**
Create a program that gives clothing advice based on temperature input.

### 📋 **Requirements**
1. Ask the user for temperature in Celsius
2. Give appropriate clothing advice based on the temperature:
   - Below 0°C: "Wear a heavy coat!"
   - 0-10°C: "Wear a warm jacket!"
   - 11-20°C: "A light jacket is fine"
   - Above 20°C: "T-shirt weather!"

### 💻 **Template**
```python
# Get temperature from user
temperature = int(input("What's the temperature in Celsius? "))

# Your if statements go here
# Remember to use proper indentation and colons!

```

### 🔍 **Hints**
1. Use `int(input())` to get a number from the user
2. Remember the colon `:` after each if statement
3. Indent your print statements properly (4 spaces)
4. Test with different temperatures to make sure it works

### ✅ **Example Output**
```
What's the temperature in Celsius? 25
T-shirt weather!

What's the temperature in Celsius? -5
Wear a heavy coat!

What's the temperature in Celsius? 15
A light jacket is fine
```

### 🔍 **What You're Learning**
- Basic if statement syntax
- Using comparison operators (>=, <, etc.)
- Getting user input with `input()`
- Converting strings to integers with `int()`

---

## Practice 2: Login System (20 minutes)

### 🎯 **Objective**
Build a simple login system that combines logical operators and gives specific feedback for different scenarios.

### 📋 **Requirements**
1. Set a correct username and password in your program
2. Ask the user for their credentials
3. Check if BOTH username AND password are correct
4. Give appropriate messages for different scenarios:
   - Both correct: "Welcome!"
   - Wrong username only: "Username not found"
   - Wrong password only: "Incorrect password"
   - Both wrong: "Invalid credentials"

### 💻 **Template**
```python
# Set the correct credentials
correct_username = "admin"
correct_password = "secret123"

# Get user input
username = input("Enter username: ")
password = input("Enter password: ")

# Your logic goes here
# Use logical operators (and, or, not) to check different scenarios
# Remember: you need to check all four possible combinations!

```

### 🔍 **Hints**
1. Use `and` to check if both conditions are true
2. Use `==` to compare strings (not `=`)
3. Think about the order of your conditions
4. You'll need multiple `elif` statements for different scenarios

### ✅ **Example Output**
```
Enter username: admin
Enter password: secret123
Welcome!

Enter username: admin
Enter password: wrong
Incorrect password

Enter username: hacker
Enter password: secret123
Username not found

Enter username: hacker
Enter password: wrong
Invalid credentials
```

### 🚀 **Challenge Extensions** (Optional)
If you finish early, try adding:
- Multiple valid users (store in variables)
- Account lockout after 3 failed attempts
- Different access levels (admin vs regular user)

### 🔍 **What You're Learning**
- Logical operators (and, or, not)
- Complex conditional logic with elif chains
- String comparisons
- Handling multiple scenarios in decision-making

---

## 📚 Key Concepts Review

After completing these practice, you should understand:

### Comparison Operators:
- `==` (equal to) vs `=` (practice)
- `!=` (not equal to)
- `<`, `>`, `<=`, `>=` (less than, greater than, etc.)
- How to compare both numbers and strings

### Conditional Statements:
- `if` statement syntax (with colons and indentation)
- `elif` for multiple conditions
- `else` as a catch-all
- Why order matters in elif chains

### Logical Operators:
- `and` - ALL conditions must be True
- `or` - At least ONE condition must be True  
- `not` - Flips True to False and vice versa
- How to combine multiple conditions

### Error Handling:
- `try/except` blocks for handling errors gracefully
- `ValueError` for invalid number conversions
- Why error handling prevents program crashes

### Real-World Applications:
- Decision-making logic in programs
- User input validation
- Building interactive applications
- Handling edge cases and invalid input

### Best Practices:
- Proper indentation (4 spaces consistently)
- Clear variable names
- Testing with different inputs
- Providing helpful error messages

**Remember**: Control flow is what makes programs "smart" - they can make decisions just like humans do. Master these concepts and your programs will be able to respond intelligently to different situations! 