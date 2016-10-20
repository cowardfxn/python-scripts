#!/usr/bin/python
# encoding: utf-8

'''
mysql的Python驱动测试

'''

import mysql.connector
from mysql.connector import errorcode
from __future__ import print_function

config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'stock_test',
    'raise_on_warning': True,
    'use_pure': True
}

try:
    cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    else:
        print(err)
else:
    cnx.close()

DB_NAME = "stock_test"
TABLES = {}
TABLES["employees"] = (
    """CREATE TABLE `employees` (
            `emp_no` int(11) NOT NULL AUTO_INCREMENT,
            `birth_date` date NOT NULL,
            `first_name` varchar(14) NOT NULL,
            `last_name` varchar(16) NOT NULL,
            `gender` enum('M', 'F') NOT NULL,
            `hire_date` date NOT NULL,
            PRIMARY KEY (`emp_no`)
            ) ENGINE=InnoDB
    """
    )

TABLES["departments"] = ("""
    CREATE TABLE `departments` (
        `dept_no` char(4) NOT NULL,
        `dept_name` varchar(40) NOT NULL,
        PRIMARY KEY (`dept_no`),
        UNIQUE KEY `dept_name` (`dept_name`)
        ) ENGINE=InnoDB
    """)

TABLES["salaries"] = ("""
    CREATE TABLE `salaries` (
        `emp_no` int(11) NOT NULL,
        `salary` int(11) NOT NULL,
        `from_date` date NOT NULL,
        `to_date` date NOT NULL,
        PRIMARY KEY (`emp_no`, `from_date`), KEY `emp_no` (`emp_no`),
        CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`emp_no`)
            REFERENCES `employees` (`emp_no`) ON DELETE CASCADE
        ) ENGINE=InnoDB
    """)

TABLES["dept_emp"] = ("""
    CREATE TABLE `dept_emp` (
        `emp_no` int(11) NOT NULL,
        `dept_no` char(4) NOT NULL,
        `from_date` date NOT NULL,
        `to_date` date NOT NULL,
        PRIMARY KEY (`emp_no`, `dept_no`), KEY `emp_no` (`emp_no`),
        KEY `dept_no` (`dept_no`),
        CONSTRAINT `dept_emp_ibfk_1` FOREIGN KEY (`emp_no`)
            REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,
        CONSTRAINT `dept_emp_ibfk_2` FOREIGN KEY (`dept_no`)
            REFERENCES `departments` (`dept_no`) ON DELETE CASCADE
        ) ENGINE=InnoDB
    """)

TABLES["dept_manager"] = ("""
    CREATE TABLE `dept_manager` (
        `dept_no` char(4) NOT NULL,
        `emp_no` int(11) NOT NULL,
        `from_date` date NOT NULL,
        `to_date` date NOT NULL,
        PRIMARY KEY (`emp_no`, `dept_no`),
        KEY `emp_no` (`emp_no`),
        KEY `dept_no` (`dept_no`),
        CONSTRAINT `dept_manager_ibfk_1` FOREIGN KEY (`emp_no`)
            REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,
        CONSTRAINT `dept_manager_ibfk_2` FOREIGN KEY (`dept_no`)
            REFERENCES `departments` (`dept_no`) ON DELETE CASCADE
        ) ENGINE=InnoDB
    """)

TABLES["titles"] = ("""
    CREATE TABLE `titles` (
        `emp_no` int(11) NOT NULL,
        `title` varchar(50) NOT NULL,
        `from_date` date NOT NULL,
        `to_date` date DEFAULT NULL,
        PRIMARY KEY (`emp_no`, `title`, `from_date`), KEY `emp_no` (`emp_no`),
        CONSTRAINT `titles_ibfk_1` FOREIGN KEY (`emp_no`)
            REFERENCES `employees` (`emp_no`) ON DELETE CASCADE
        ) ENGINE=InnoDB
    """)

cursor = cnx.cursor()

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cnx.database = DB_NAME
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for name, ddl in TABLES.iteritems():
    try:
        print("Create table {}:".format(name))
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()


from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root', database="localtest", host="localhost")
cursor = cnx.cursor()

tomorrow = datetime.now().date() + timedelta(days=1)

add_employee = ("INSERT INTO employees (first_name, last_name, hire_date, gender, birth_date) VALUES (%s, %s, %s, %s, %s)")
add_salary = ("INSERT INTO salaries (emp_no, salary, from_date, to_date) VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")

data_employee = ("Geert", "Vanderkelen", tomorrow, "M", date(1977, 6, 14))

cursor.execute(add_employee, data_employee)
emp_no = cursor.lastrowid

data_salary = {
    'emp_no': emp_no,
    'salary': 50000,
    'from_date': tomorrow,
    'to_date': date(9999, 1, 1)
}

cursor.execute(add_salary, data_salary)

cnx.commit()

cursor.close()
cnx.close()
