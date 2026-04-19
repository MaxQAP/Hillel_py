import pytest
import allure
from homework30 import session, Student, add_new_student, update_student_name, delete_student

@allure.feature("Student Management CRUD")
def test_db_connection():
    with allure.step("Перевірка активності сесії бази даних"):
        assert session.is_active is True

@allure.feature("Student Management CRUD")
def test_crud_operations():
    with allure.step("Створення нового студента"):
        add_new_student("QA Tester", 1)
        student = session.query(Student).filter_by(name="QA Tester").first()
        assert student is not None

    with allure.step("Оновлення імені студента"):
        update_student_name(student.id, "New Name")
        session.refresh(student)
        assert student.name == "New Name"

    with allure.step("Видалення студента з бази"):
        s_id = student.id
        delete_student(s_id)
        deleted_student = session.query(Student).get(s_id)
        assert deleted_student is None