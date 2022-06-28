# Creating the admin privileges
import mysql.connector

from mysql.connector import cursor


def admin():
    # importing libraries
    import mysql.connector

    # setting up a connection to mysql
    conn = mysql.connector.connect(host="localhost", user="root", passwd="@aD611624")
    cursor = conn.cursor()

    # Creating a new database
    cursor.execute("create database sms3")
    cursor.execute('use sms3')

    # Creating admin table
    admin_table = """create table admin(
    username varchar(20) not null, password varchar(20) not null, first_name varchar(20) not null,
    last_name varchar(20) not null, position varchar(20) not null
    );"""
    cursor.execute(admin_table)

    # Inserting admin data
    admin_data = """insert into admin values(
        "admin","2022","Seth","Aduful","Administrator")"""
    cursor.execute(admin_data)


def create_tables():
    conn = mysql.connector.connect(host="localhost", user="root", passwd="@aD611624")
    cursor = conn.cursor()
    cursor.execute('use sms3')
    # create school table
    school_table = """create table school_table(
        sch_name varchar(50) not null, sch_type varchar(30) not null, population int(6) not null,
        est_date date not null);"""
    cursor.execute(school_table)

    student_table = """create table student_info(
        stu_id int(4) primary key,
        first_name varchar(20) not null,
        last_name varchar(20) not null,
        date_of_birth date not null,
        gender char not null,
        religion varchar(50),
        class int not null,
        hometown varchar(50) not null
        );"""
    cursor.execute(school_table)

    staff_table = """create table staff_info(
        staff_id int(4) primary key, first_name varchar(20) not null, last_name varchar(20) not null, 
        date_of_birth date not null,
        gender char not null,
        religion varchar(50),
        class int not null,
        adm_post varchar(50),
        subjects varchar(40)
        )"""
    cursor.execute(staff_table)


def home():
    conn = mysql.connector.connect(host="localhost", user="root", passwd="@aD611624")
    cursor = conn.cursor()
    cursor.execute('use sms3')
    greeting = "Hello there, welcome to the school management system."
    print("Admin Login Info:")
    admin_name = input("Name of admin: ")
    admin_user_name = input("Admin user name: ")
    admin_pass = input("Admin password: ")
    det = cursor.execute("select username,password from admin")
    print(det)
    db_username = det[0]
    db_password = det[1]
    if admin_user_name == db_username and admin_pass == db_password:
        create_tables()
    else:
        home()


#admin()
home()
