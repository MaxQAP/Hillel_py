class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


#emp = Employee("Maxim", 2000)
#print(emp.name)
#print(emp.salary)

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

#mngr = Manager("Alex", 2500, "Project Manager")
#print(mngr.name)
#print(mngr.salary)
#print(mngr.department)
#print(f"У нашій компанді є {mngr.department} його звуть {mngr.name} його зарплата у долларах - {mngr.salary}")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

#dev = Developer("Lera", 1350, "Python")
#print(dev.name)
#print(dev.salary)
#print(dev.programming_language)
#print(f"У нас є {dev.name}, яка пише на {dev.programming_language} ,її зарплата {dev.salary} долларів.")

class Teamlead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer. __init__(self, name, salary, programming_language)
        self.team_size = team_size

tl = Teamlead("Sasha", 5000,department="Developer", programming_language="Javascript", team_size=5)
#print(tl.name)
#print(tl.salary)
#print(tl.department)
#print(tl.programming_language)
#print(tl.team_size)
#print(f"TeamLead: {tl.name}, відділ: {tl.department}, мова: {tl.programming_language}, к-ть у команді: {tl.team_size} людей")

print("\nПеревірка наявності атрибутів TeamLead:")
print("  name :", hasattr(tl, "name"))
print("  salary :", hasattr(tl, "salary"))
print("  department (Manager):", hasattr(tl, "department"))
print("  programming_language (Developer):", hasattr(tl, "programming_language"))
print("  team_size :", hasattr(tl, "team_size"))

