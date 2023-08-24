from datetime import datetime, date, timedelta
import faker
from random import randint, choice
import sqlite3
from pprint import pprint


fake = faker.Faker('uk-UA')

disciplines = [
    'Вища математика',
    "Дискретна математика",
    "Програмування",
    "Теорія основ електроенергетики",
    "Історія України",
    "Англійська мова",
    "Креслення",
    "Філософія"
]

groups = [
    'ІН-31',
    'ІН-32',
    'ІН-33',
    'ЕТ-31',
    'ЕЛ-31'
]

NUMBER_TEACHERS = 5
NUMBER_STUDENTS = 50


connect = sqlite3.connect('data.db')
cur = connect.cursor()


def seed_teachers():
    teachers_ = [fake.name() for _ in range(NUMBER_TEACHERS)]
    sql = "INSERT INTO teachers(fullname) VALUES(?)"
    cur.executemany(sql, zip(teachers_,))


def seed_disciplines():
    sql = 'INSERT INTO disciplines(name, teacher_id) VALUES(?, ?)'
    cur.executemany(sql, zip(disciplines, iter(randint(1, NUMBER_TEACHERS) for _ in disciplines)))


def seed_groups():
    sql = 'INSERT INTO groups(name) VALUES(?)'
    cur.executemany(sql, zip(groups,))


def seed_students():
    students = [fake.name() for _ in range(NUMBER_STUDENTS)]
    sql = 'INSERT INTO students(fullname, group_id) VALUES(?, ?)'
    cur.executemany(sql, zip(students, iter(randint(1, len(groups)) for _ in students)))


def get_list_date(start: date, end: date) -> list[date]:
    result = []
    current_date = start
    while current_date <= end:
        if current_date.isoweekday() < 6:
            result.append(current_date)
        current_date += timedelta(1)
    return result


def seek_grades():
    start_date = datetime.strptime('2023-09-01', "%Y-%m-%d")
    end_date = datetime.strptime('2024-06-15', "%Y-%m-%d")
    sql = 'INSERT INTO grades(discipline_id, student_id, grade, date_of) VALUES(?, ?, ?, ?)'
    list_dates = get_list_date(start_date, end_date)
    grades = []
    for day in list_dates:
        random_discipline = randint(1, len(disciplines))
        random_students = [randint(1, NUMBER_STUDENTS) for _ in range(5)]
        for student in random_students:
            grades.append((random_discipline, student, randint(1, 5), day.date()))
    cur.executemany(sql, grades)



if __name__ == '__main__':
    try:
        seed_teachers()
        seed_disciplines()
        seed_groups()
        seed_students()
        seek_grades()
        connect.commit()

    # except sqlite3.Error as e:
    #     pprint(e)
    finally:
        connect.close()

