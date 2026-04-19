import os
import time
import random
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, exc
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from faker import Faker


DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///students.db')

Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=False)
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



def seed_data():
    """Заповнення бази початковими даними"""
    course_names = ["QA", "Project manager", "Java", "SMM", "Developers"]
    courses = [Course(title=name) for name in course_names]
    session.add_all(courses)
    session.commit()

    fake = Faker()
    for _ in range(20):
        student = Student(name=fake.name())
        random_course = random.choice(courses)
        student.courses = [random_course]
        session.add(student)

    session.commit()
    print("База даних заповнена початковими даними!")


def add_new_student(name, course_id):
    new_student = Student(name=name)
    course = session.get(Course, course_id)
    if course:
        new_student.courses.append(course)
        session.add(new_student)
        session.commit()
        print(f"Додано: {name} на курс '{course.title}'")
    return new_student


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
        print(f"Дані студента {student_id} оновлено на '{new_name}'.")


def delete_student(student_id):
    student = session.get(Student, student_id)
    if student:
        session.delete(student)
        session.commit()
        print(f"Студента ID:{student_id} видалено.")



def init_db():

    retries = 5
    while retries > 0:
        try:
            Base.metadata.drop_all(engine)
            Base.metadata.create_all(engine)
            print("Таблиці створено успішно.")
            break
        except exc.OperationalError:
            print(f"База ще не готова, (спроб залишилось: {retries})")
            retries -= 1
            time.sleep(3)
    else:
        print("Не вдалося підключитися до бази даних.")
        exit(1)


if __name__ == "__main__":
    init_db()
    seed_data()

    add_new_student("Maxim Lazarets", 1)

    print("\n Студенти на курсі 'QA':")
    qa_students = get_students_by_course(1)
    for s in qa_students:
        print(f"- {s.name}")

    update_student_name(1, "Maxim Updated")
    delete_student(10)

    print("\n Додаток завершив роботу.")