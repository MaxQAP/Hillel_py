class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language


class Teamlead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

def test_teamlead_attributes():

    tl = Teamlead("Sasha", 5000, department="Developer", programming_language="Javascript", team_size=5)
    #tl = Teamlead("Sasha", Max, department="QA", programming_language="Python", team_size=3)
    assert tl.name == "Sasha",                          "Неправильне ім'я"
    assert tl.salary == 5000,                            "Неправильна зарплата"
    assert tl.department == "Developer",                "Неправильний відділ"
    assert tl.programming_language == "Javascript",     "Неправильна мова програмування"
    assert tl.team_size == 5,                           "Неправильний розмір команди"
    print("Тест пройшов успішно")

if __name__ == "__main__":
    test_teamlead_attributes()