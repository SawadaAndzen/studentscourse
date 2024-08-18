import sqlite3

base = sqlite3.connect("studentscourse/my_db.db")
conn = base.cursor()

conn.execute('''
             CREATE TABLE IF NOT EXISTS students(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name VARCHAR NOT NULL,
                 age INTEGER NOT NULL,
                 major VARCHAR NOT NULL
             );
             ''')

conn.execute('''
             CREATE TABLE IF NOT EXISTS courses(
                 course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 course_name VARCHAR NOT NULL,
                 instructor VARCHAR NOT NULL
             );
             ''')

conn.execute('''
             CREATE TABLE IF NOT EXISTS relation(
                course_id INTEGER,
                student_id INTEGER,
                FOREIGN KEY (course_id) REFERENCES courses(course_id),
                FOREIGN KEY (student_id) REFERENCES students(id)      
            );
             ''')

base.commit()

while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("7. Вийти")
    
    choice = input("Оберіть опцію (1-7): ")

    if choice == "1":
        _name = input("Ім'я: ")
        _age = input("Вік: ")
        _major = input("Спеціалізація: ")
        
        conn.execute('''
                     INSERT INTO students(name, age, major) VALUES(?, ?, ?);
                     ''', (_name, _age, _major))
        
        base.commit()

    elif choice == "2":
        _course_name = input("Назва курсу: ")
        _instructor = input("Викладач: ")
        
        conn.execute('''
                     INSERT INTO courses(course_name, instructor) VALUES(?, ?);
                     ''', (_course_name, _instructor))
        
        base.commit()

    elif choice == "3":
        ...
     
    elif choice == "4":
        ...

    elif choice == "5":
        _student_id = input("ID студента: ")
        _course_id = input("ID курсу: ")
        
        conn.execute('''
                     INSERT INTO relation(student_id, course_id) VALUES(?, ?);
                     ''', (_student_id, _course_id))
        
        base.commit()

    elif choice == "6":
        ...
       
    elif choice == "7":
        break

    else:
        print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")