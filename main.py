from employee import Employee, Manager

# Create employee using normal constructor
emp1 = Employee("Alice", 30)

# Create employee using class method (alternative constructor)
emp2 = Employee.from_string("Bob-25-Developer")

# Create a manager and assign existing employees (Aggregation)
mgr = Manager("Eve", 40, employees=[emp1, emp2])

# Set address for both employees using the nested Address class
emp1.set_address("123 Elm St", "Metro City")
emp2.set_address("456 Oak St", "River Town")

# Print employee details (uses __str__ which calls get_details)
print(emp1)  # Output: Alice, 30, Employee
print(emp2)  # Output: Bob, 25, Developer

# Static method call to check age validity
print("Is Bob's age valid?", Employee.is_valid_age(emp2.age))  # True

# Manager details with overridden method showing number of employees managed
print("Manager Info:", mgr)  # Output: Eve, 40, Manager - manages 2 employee(s)

# Access address via composed object
print("Alice's Address:", emp1.address)  # Output: 123 Elm St, Metro City
