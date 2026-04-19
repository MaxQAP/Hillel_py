import pytest
from homework29 import session, Student, add_new_student, update_student_name, delete_student

def test_db_connection():
    assert session.is_active is True

def test_crud_operations():

    add_new_student("QA Tester", 1)
    student = session.query(Student).filter_by(name="QA Tester").first()
    assert student is not None

    update_student_name(student.id, "New Name")
    session.refresh(student)
    assert student.name == "New Name"

    s_id = student.id
    delete_student(s_id)
    deleted_student = session.query(Student).get(s_id)
    assert deleted_student is None