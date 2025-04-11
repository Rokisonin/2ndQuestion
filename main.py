from employee import Employee, Manager

# Constructor 1
emp1 = Employee("Alice", 30)
# Constructor 2 (classmethod)
emp2 = Employee.from_string("Bob-25-Developer")

# Manager with aggregation
mgr = Manager("Eve", 40, employees=[emp1, emp2])

# Add address using nested class
emp1.set_address("123 Elm St", "Metro City")
emp2.set_address("456 Oak St", "River Town")

# Output
print(emp1)
print(emp2)
print("Is Bob's age valid?", Employee.is_valid_age(emp2.age))
print("Manager Info:", mgr)
print("Alice's Address:", emp1.address)
