# CREATE DATA BASE IN SQLite3
# import sqlite3
import sqlite3
import random

# connection to sqlite3
# connection object
conn = sqlite3.connect("quiz.sqlite")

# cursor object
cursor_obj = conn.cursor()

# creating tables in dataset
q_table = """CREATE TABLE IF NOT EXISTS `Questions` (
    `question_id` INTEGER PRIMARY KEY, 
    `question` VARCHAR(250) NOT NULL UNIQUE, 
    `answer` VARCHAR(250) NOT NULL
);"""
op_table = """CREATE TABLE IF NOT EXISTS `Options` (
    `option_id` INTEGER PRIMARY KEY, 
    `option` VARCHAR (250) NOT NULL,
    `question_id` INTEGER,
    FOREIGN KEY (question_id) REFERENCES Questions(question_id)
);"""

cursor_obj.execute(op_table)
cursor_obj.execute(q_table)
conn.commit()

# ADD 10 Theoretical brief questions related to python
# add_questions = """INSERT INTO `Questions`(question_id,question,answer) VALUES 
# (1,'What is Python?','Python is a high-level, interpreted, interactive and object-oriented scripting language.'),
# (2,'What are the key features of Python?','Python is a high-level language and easy to learn.'),
# (3,'What are the benefits of using Python?','Python is easy to maintain and portable.'),
# (4,'What is pep 8?','PEP 8 is a coding convention, a set of recommendation, about how to write your Python code more readable.'),
# (5,'What is the purpose of PYTHONPATH environment variable?','PYTHONPATH is an environment variable which you can set to add additional directories where Python will look for modules and packages.'),
# (6,'What is the purpose of PYTHONSTARTUP environment variable?','PYTHONSTARTUP is an environment variable that contains the path of an initialization file containing Python source code.'),
# (7,'What is the purpose of PYTHONCASEOK environment variable?','PYTHONCASEOK is an environment variable that is used in Windows to instruct Python to find the first case-insensitive match in an import statement.'),
# (8,'What is the purpose of PYTHONHOME environment variable?','PYTHONHOME is an environment variable that is used in Windows to specify the location of the standard Python libraries.'),
# (9,'What is the purpose of PYTHONIOENCODING environment variable?','PYTHONIOENCODING is an environment variable that is used to specify the encoding of the standard I/O files.'),
# (10,'What is the purpose of PYTHONHASHSEED environment variable?','PYTHONHASHSEED is an environment variable that is used in Python to provide hash values which are used to set the hash seed for the random and hash functions.');"""


# cursor_obj.execute(add_questions)
# conn.commit()

# ADD OPTIONS
# add_options = """INSERT INTO `Options`(option_id,option,question_id) VALUES (1, 'Python is a high-level, interpreted, interactive, and object-oriented scripting language.', 1),
# (2, 'Python is a high-level language and easy to learn.', 1),
# (3, 'Python is easy to maintain and portable.', 1),
# (4, 'PEP 8 is a coding convention, a set of recommendations on how to write Python code more readable.', 1),

# (5, 'Python is a high-level language and easy to learn.', 2),
# (6, 'PYTHONSTARTUP is an environment variable that contains the path of an initialization file containing Python source code.', 2),
# (7, 'PYTHONCASEOK is an environment variable that is used in Windows to instruct Python to find the first case-insensitive match in an import statement.', 2),
# (8, 'PYTHONHOME is an environment variable that is used in Windows to specify the location of the standard Python libraries.', 2),

# (9, 'PYTHONIOENCODING is an environment variable that is used to specify the encoding of the standard I/O files.', 3),
# (10, 'PYTHONHASHSEED is an environment variable used to provide hash values for random and hash functions.', 3),
# (11, 'PYTHONFAULTHANDLER enables Python to dump the Python traceback explicitly on a crash.', 3),
# (12, 'Python is easy to maintain and portable.', 3),

# (13, 'Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.', 4),
# (14, 'Flask is a lightweight WSGI web application framework in Python.', 4),
# (15, 'FastAPI is a modern, fast (high-performance) web framework for building APIs with Python.', 4),
# (16, 'PEP 8 is a coding convention, a set of recommendation, about how to write your Python code more readable.', 4),

# (17, 'Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming.', 5),
# (18, 'Python does not have built-in support for low-level programming.', 5),
# (19, 'Python provides support for automatic memory management.', 5),
# (20, 'PYTHONPATH is an environment variable which you can set to add additional directories where Python will look for modules and packages.', 5),

# (21, 'In Python, a list is an ordered collection of elements that can contain items of different data types.', 6),
# (22, 'A tuple is similar to a list but immutable.', 6),
# (23, 'Dictionaries are collections of key-value pairs.', 6),
# (24, 'PYTHONSTARTUP is an environment variable that contains the path of an initialization file containing Python source code.', 6),

# (25, 'NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices.', 7),
# (26, 'Pandas is a fast, powerful, flexible, and easy-to-use data analysis and data manipulation library built on top of NumPy.', 7),
# (27, 'Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.', 7),
# (28, 'PYTHONCASEOK is an environment variable that is used in Windows to instruct Python to find the first case-insensitive match in an import statement.', 7),

# (29, 'A Python class is a blueprint for creating objects.', 8),
# (30, 'Python supports inheritance, which allows a new class to inherit methods and properties from an existing class.', 8),
# (31, 'Polymorphism in Python allows methods to do different things based on the object type it is acting upon.', 8),
# (32, 'PYTHONHOME is an environment variable that is used in Windows to specify the location of the standard Python libraries.', 8),

# (33, 'In Python, exceptions are errors detected during execution.', 9),
# (34, 'Exceptions in Python can be handled using try, except, and finally blocks.', 9),
# (35, 'The raise statement allows the programmer to force a specific exception to occur.', 9),
# (36, 'PYTHONIOENCODING is an environment variable that is used to specify the encoding of the standard I/O files.', 9),

# (37, 'PIP is a package management system used to install and manage software packages written in Python.', 10),
# (38, 'Conda is an open-source package management system and environment management system.', 10),
# (39, 'Virtualenv is a tool to create isolated Python environments.', 10),
# (40, 'PYTHONHASHSEED is an environment variable that is used in Python to provide hash values which are used to set the hash seed for the random and hash functions.', 10);"""

# cursor_obj.execute(add_options)
# conn.commit()

# UPDATE OPTIONS
# update_option1 = """UPDATE `Options` SET `question_id` = '5' WHERE `option_id` = 1;"""
# update_option2 = """UPDATE `Options` SET `question_id` = '3' WHERE `option_id` = 2;"""
# update_option3 = """UPDATE `Options` SET `question_id` = '2' WHERE `option_id` = 3;"""
# update_option4 = """UPDATE `Options` SET `question_id` = '9' WHERE `option_id` = 4;"""
# cursor_obj.execute(update_option1)
# cursor_obj.execute(update_option2)
# cursor_obj.execute(update_option3)
# cursor_obj.execute(update_option4)
# conn.commit()

# REMOVE OPTIONS
# del_row = """DELETE FROM `Options` WHERE `option_id` = 3;"""
# cursor_obj.execute(del_row)
# conn.commit()


#---------------START QUIZ IMPLEMENTATION--------------#
# prompt user to select one of the options
print("Select one of the options: \n1. Login as Admin\n2. Login as User\n")
user_ans = input("Enter the option: ")
if user_ans == "1":
    # login as admin
    def_password = "admin123"
    password = input("Enter the password: ")
    print("")
    if password == def_password:
        print("Logged in as Admin!!\n")
        # prompt user to select one of the options
        print("Select one of the options: \n1. Add Question\n2. Update Question\n3. Delete Question\n4. View Questions\n5. Exit\n")
        user_option = input("Enter the option: ")
        if user_option == "1":
            # add question
            question = input("Enter the question: ")
            answer = input("Enter the answer: ")
            add_question = f"INSERT INTO `Questions`(question,answer) VALUES ('{question}','{answer}');"
            cursor_obj.execute(add_question)
            conn.commit()
            print("Question added successfully")
            # add options
            question_id = cursor_obj.lastrowid
            for i in range(4):
                option = input(f"Enter option {i+1}: ")
                add_option = f"INSERT INTO `Options`(option,question_id) VALUES ('{option}',{question_id});"
                cursor_obj.execute(add_option)
                conn.commit()
            print("Options added successfully")
            exit()
        elif user_option == "2":
            # update question
            question_id = input("Enter the question id: ")
            question = input("Enter the question: ")
            answer = input("Enter the answer: ")
            update_question = f"UPDATE `Questions` SET `question` = '{question}', `answer` = '{answer}' WHERE `question_id` = {question_id};"
            cursor_obj.execute(update_question)
            conn.commit()
            print("Question updated successfully")
            exit()
        elif user_option == "3":
            # delete question
            question_id = input("Enter the question id: ")
            del_question = f"DELETE FROM `Questions` WHERE `question_id` = {question_id};"
            cursor_obj.execute(del_question)
            conn.commit()
            print("Question deleted successfully")
            exit()
        elif user_option == "4":
            # view questions
            view_question = "SELECT * FROM `Questions`;"
            cursor_obj.execute(view_question)
            questions = cursor_obj.fetchall()
            for question in questions:
                print(f"Question ID: {question[0]}\nQuestion: {question[1]}\nAnswer: {question[2]}\n")
            exit()
        elif user_option == "5":
            exit()
    else:
        print("Wrong Password !")
        exit()
elif user_ans == "2":
    print("Logged in as User\n")
    print("Get yourself ready for Python Quiz !!\n")
    # display randomly selected 5 questions
    score = 0
    for i in range(5):
        # select random question
        select_question = "SELECT * FROM `Questions` ORDER BY RANDOM() LIMIT 1;"
        cursor_obj.execute(select_question)
        question = cursor_obj.fetchone()
        print(f"Question: {question[1]}\n")
        # display options
        select_options = f"SELECT * FROM `Options` WHERE `question_id` = {question[0]};"
        cursor_obj.execute(select_options)
        options = cursor_obj.fetchall()
        i=1
        for i,option in enumerate(options,start=1  ):
            print(f"{i}. {option[1]}\n")
            i += 1
        user_ans = input("Enter your answer: ")
        if user_ans == question[2]:
            print("Correct Answer !!")
            score += 1
        else:
            print("Wrong Answer !!")
    print("")
    print(f"Your score is: {score}/5")
    print("Thank you for participating in the quiz !!")
    print("")
else:
    print("Invalid Option !")
    exit()