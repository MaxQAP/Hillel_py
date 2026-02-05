class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        # Явно викликаємо Employee (без super)
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        # Явно викликаємо Employee (без super)
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        # Явно викликаємо __init__ від Manager
        Manager.__init__(self, name, salary, department)

        # Явно викликаємо __init__ від Developer
        Developer.__init__(self, name, salary, programming_language)

        self.team_size = team_size


# Тест
tl = TeamLead("Sasha", 5000, department="Developer", programming_language="Javascript", team_size=2)

print(tl.name)
print(tl.salary)
print(tl.department)
print(tl.programming_language)
print(tl.team_size)

