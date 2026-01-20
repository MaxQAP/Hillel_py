class student:
    def __init__(self, name: str, surname: str, age: int, average_score: float ):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = average_score

    def __str__(self):
        return f'{self.name}, {self.surname}, {self.age}, {self.average_score}'

#student_1 = student("Maxim", "Lazarets", 28, 91.5)
#print(student_1.name)
#print(student_1.surname)
#print(student_1.age)
#print(student_1.average_score)

    def set_average_score (self, new_score: float):
        if 0 <= new_score <= 100:
            old_score = self.average_score
            self.average_score = new_score
            print(f"Бал {old_score} змінено на: {new_score}")
        else:
            print(f"Помилка! {new_score} - число не вірне")

student_1 = student("Maxim", "Lazarets", 28, 91.5)
print(student_1.name)
print(student_1.surname)
print(student_1.age)
print(student_1.average_score)
print()

print(student_1)
print()
student_1.set_average_score(95)
#student_1.set_average_score(101) - приклад для виведення помилки

print("Змінений середній бал:",student_1.average_score)

