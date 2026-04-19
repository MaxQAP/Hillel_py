from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
import random

Base = declarative_base()
engine = create_engine('sqlite:///students.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

student_courses = Table(
    'student_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship('Course', secondary=student_courses, back_populates='students')

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}')>"


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    students = relationship('Student', secondary=student_courses, back_populates='courses')

    def __repr__(self):
        return f"<Course(title='{self.title}')>"

Base.metadata.create_all(engine)

from faker import Faker
fake = Faker()

def seed_data():
    course_names = ["QA", "Project manager", "Java", "SMM", "Developers"]
    courses = [Course(title=name) for name in course_names]
    session.add_all(courses)

    #for _ in range(20): # тут я створюю таблицю щоб студенти вибирали декілька курсів
     #   student = Student(name=fake.name())
      #  student.courses = random.sample(courses, k=random.randint(1, 3))
       # session.add(student)

    for _ in range(20): # тут вже 1 студент = 1 курс
        student = Student(name=fake.name())
        random_course = random.choice(courses)
        student.courses = [random_course]
        session.add(student)

    session.commit()
    print("База даних заповнена!")
    session.commit()


def add_new_student(name, course_id):
    new_student = Student(name=name)
    course = session.get(Course, course_id)
    if course:
        new_student.courses.append(course)
        session.add(new_student)
        session.commit()
        print(f"Додано: {name} на курс '{course.title}'")

def get_students_by_course(course_id):
    course = session.get(Course, course_id)
    return course.students if course else []

def get_courses_by_student(student_id):
    student = session.get(Student, student_id)
    return student.courses if student else []

def update_student_name(student_id, new_name):
    student = session.get(Student, student_id)
    if student:
        student.name = new_name
        session.commit()
        print(f"Дані студента {student_id} оновлено.")

def delete_student(student_id):
    student = session.get(Student, student_id)
    if student:
        session.delete(student)
        session.commit()
        print(f"Студента {student_id} видалено.")



if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    seed_data()

    add_new_student("Maxim Lazarets", 1)

    print("\nСтуденти на курсі 'QA':")
    math_students = get_students_by_course(1)
    for s in math_students:
        print(f"- {s.name}")

    print(f"\nКурси студента №7:")
    courses = get_courses_by_student(7)
    for c in courses:
        print(f"- {c.title}")

    update_student_name(1, "Stas Serkov")
    delete_student(10)