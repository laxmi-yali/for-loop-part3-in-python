# Problems using a for loop
# 1. Student marks total
# Problem: A teacher wants to calculate the total marks obtained by a student in 5 subjects.

marks = [80, 75, 90, 85, 70]
total = 0

for mark in marks:
    total = total + mark

print("Total marks:", total)
print("Average marks:", total / 5)

# 2. Shopping bill calculator
# Problem: A customer buys 4 products. Calculate the total bill.

prices = [100, 250, 50, 150]
total = 0

for price in prices:
    total += price

print("Total bill: ₹", total)

# 3. Electricity unit calculation
# Problem: Display the electricity units consumed each day for 7 days.

units = [5, 6, 4, 7, 5, 8, 6]
day = 1

for unit in units:
    print("Day", day, ":", unit, "units")
    day += 1
    
""" Part 2: Problems using a nested for loop
A nested for loop means writing one for loop inside another for loop.
4. Classroom attendance system
Problem: A college has 3 classrooms, and each classroom has 4 students. Display student numbers for every classroom."""

for classroom in range(1, 4):
    print("Classroom", classroom)

    for student in range(1, 5):
        print("Student", student)
        
# 5. Employee salary report
# Problem: A company has 3 employees. Display the salary for each employee over 2 months.

salaries = [
    [20000, 22000],
    [25000, 26000],
    [30000, 32000]
]

for employee in range(3):
    print("Employee", employee + 1)

    for month in range(2):
        print("Month", month + 1, "salary:",
              salaries[employee][month])
        
# Generate a multiplication table
# Problem: A teacher wants to display multiplication tables from 1 to 3, up to 5 multiples.

for i in range(1, 4):
    print("Table of", i)

    for j in range(1, 11):
        print(i, "x", j, "=", i * j)

    print()