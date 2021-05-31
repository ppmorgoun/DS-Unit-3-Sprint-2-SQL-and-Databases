import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# Creating a list of the 10 most expensive items
expensive_items = 'SELECT UnitPrice, ProductName FROM Product ORDER BY UnitPrice DESC LIMIT 10'
print(curs.execute(expensive_items).fetchall())

# Retrieving the average age of employees at time of hire
avg_hire_age = 'SELECT AVG(HireDate - BirthDate) FROM employee'
print(curs.execute(avg_hire_age).fetchall())

# Retrieving the average age of employees at time of hire by city
avg_age_by_city = 'SELECT CITY, AVG(HireDate - BirthDate) FROM employee GROUP BY CITY'
print(curs.execute(avg_age_by_city).fetchall())

# Retrieving the 10 most expensive products in the database
expensive_items = 'SELECT UnitPrice, ProductName FROM Product ORDER BY UnitPrice DESC LIMIT 10'
print(curs.execute(expensive_items).fetchall())

# Retrieving the average age of employees at the time of hire
avg_hire_age = 'SELECT AVG(HireDate - BirthDate) FROM employee'
print(curs.execute(avg_hire_age).fetchall())

# Retrieving the average age of employees at the time of hire for each city
avg_age_by_city = 'SELECT CITY, AVG(HireDate - BirthDate) FROM employee GROUP BY CITY'
print(curs.execute(avg_age_by_city).fetchall())

# Selecting the ten most expensive products including the supplier company name
ten_most_expensive = 'SELECT UnitPrice, ProductName, CompanyName ' \
                     'FROM Product LEFT JOIN Supplier ON Product.SupplierId = Supplier.Id ORDER BY UnitPrice DESC LIMIT 10'
print(curs.execute(ten_most_expensive).fetchall())

# Selecting the largest product category
largest_category = 'SELECT MAX(total), CategoryName FROM' \
                   '(SELECT CategoryName, COUNT(*) AS total ' \
                   'FROM Product LEFT JOIN Category ON Product.CategoryId = Category.Id)'
print(curs.execute(largest_category).fetchall())

# Selecting the employee's first name and last name with the most territories
most_territories = 'SELECT FirstName, LastName, MAX(territories) FROM ' \
                   '(SELECT FirstName, LastName, COUNT(*) AS territories' \
                   ' FROM EmployeeTerritory LEFT JOIN Employee ON EmployeeTerritory.EmployeeId = Employee.Id GROUP BY LastName)'
print(curs.execute(most_territories).fetchall())