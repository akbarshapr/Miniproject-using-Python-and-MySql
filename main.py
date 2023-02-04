# STUDENT MANAGEMENT SYSTEM
import mysql.connector as ms

print("""
        =================================
        W E L C O M E  T O  L U M I N A R 
        =================================
""")

cn = ms.connect(host="localhost", user="root", passwd="Jas@123")
cur = cn.cursor()
cur.execute("create database if not exists student_project")
cur.execute("use student_project")

# TABLES
cur.execute("CREATE TABLE if not exists students (name VARCHAR(30) PRIMARY KEY , course VARCHAR(30), contact INT,\
            address VARCHAR(50), gender VARCHAR(20))")
cur.execute("CREATE TABLE if not exists mentors (name VARCHAR(30) PRIMARY KEY, course VARCHAR(30))")
cur.execute("CREATE TABLE if not exists student_reg (username VARCHAR(30) PRIMARY KEY, password VARCHAR(30))")
cur.execute("CREATE TABLE if not exists mentor_reg (username VARCHAR(30) PRIMARY KEY, password VARCHAR(30))")
cur.execute("CREATE TABLE if not exists assignment (question VARCHAR(30) PRIMARY KEY, submit_date VARCHAR(30))")
cur.execute("CREATE TABLE if not exists admin (username VARCHAR(30) PRIMARY KEY, password VARCHAR(30))")

# ADMIN
u = "admin"
p = "007"
cur.execute("insert ignore into admin values('" + u + "','" + p + "')")
cn.commit()


# SIGNUP AND LOGIN
def basic_features():
    print("1. SIGNUP")
    print("2. LOGIN")

    choice1 = int(input("Enter a choice: "))
    if choice1 == 1:
        signup()
    elif choice1 == 2:
        login()
    else:
        print("Invalid choice redirecting to home page")
        basic_features()

# SIGNUP


def signup():
    print("1. SIGNUP AS USER")
    print("2. SIGNUP AS MENTOR")
    choice2 = int(input("Enter a choice: "))

    if choice2 == 1:
        print("""
                ============================================
                    Please enter new registration details
                ============================================
                                                            """)
        u1 = input("Enter username : ")
        p1 = input("Enter password : ")
        cur.execute("insert into student_reg values('" + u1 + "','" + p1 + "')")
        cn.commit()
        print("""
                ========================================================
                        Congratulations!! New User Created !!
                ========================================================
                                                            """)
        signup_user()

    elif choice2 == 2:
        print("""
                ============================================
                    Please enter new registration details
                ============================================
                                                            """)
        u2 = input("Enter username : ")
        p2 = input("Enter password : ")
        cur.execute("insert into mentor_reg values('" + u2 + "','" + p2 + "')")
        cn.commit()
        print("""
                ========================================================
                        Congratulations!! New User Created !!
                ========================================================
                                                            """)
        signup_mentor()

    else:
        print("Invalid choice redirecting to home page!!")
    basic_features()


def signup_user():
    print("Signup successful. User Type... Redirecting to home")


def signup_mentor():
    print("Signup successful. User Type... Redirecting to home")


# LOGIN
def login():
    print("1. LOGIN AS ADMINISTRATOR")
    print("2. LOGIN AS STUDENT USER")
    print("3. LOGIN AS MENTOR USER")
    print("4. GO BACK")
    a = int(input("Enter a choice: "))

    # ADMIN
    if a == 1:
        print("""
                ==========================================================
                                  LOGIN AS ADMINISTRATOR
                ==========================================================
                                                            """)
        usr = input("Username : ")
        psd = input("Password : ")
        cur.execute("select password from admin where username='" + usr + "'")
        rec = cur.fetchall()
        for i in rec:
            a = list(i)
            if a[0] == str(psd):
                def main_menu1():
                    print("""
                                1. VIEW DETAILS
                                2. ADD DETAILS
                                3. DELETE
                                4. EDIT DETAILS
                                5. LOGOUT
                                                            """)
                    ch1 = int(input("Enter a choice: "))

                    # View details
                    if ch1 == 1:
                        def view_details():
                            print("""
                                    1. STUDENTS
                                    2. MENTORS
                                    3. STUDENT USERS
                                    4. MENTOR USERS
                                    5. GO BACK
                                                                """)
                            b = int(input("Enter a choice: "))
                            if b == 1:
                                cur.execute("SELECT * from students")
                                result = cur.fetchall()
                                for row in result:
                                    print(row)
                                print("**MENU**")
                                view_details()
                            elif b == 2:
                                cur.execute("SELECT * from mentors")
                                result = cur.fetchall()
                                for row in result:
                                    print(row)
                                print("**MENU**")
                                view_details()
                            elif b == 3:
                                cur.execute("SELECT * from student_reg")
                                result = cur.fetchall()
                                for row in result:
                                    print(row)
                                print("**MENU**")
                                view_details()
                            elif b == 4:
                                cur.execute("SELECT * from mentor_reg")
                                result = cur.fetchall()
                                for row in result:
                                    print(row)
                                print("**MENU**")
                                view_details()
                            elif b == 5:
                                print("BACK TO MAIN MENU")
                                main_menu1()
                            else:
                                print("Invalid Input")
                        view_details()

                    # Add details
                    elif ch1 == 2:
                        def add_details():
                            print("""
                                    1. STUDENTS
                                    2. MENTORS
                                    3. GO BACK
                                                                """)
                            c = int(input("Enter a choice: "))
                            if c == 1:
                                print("---> Add Students <---")
                                name1 = input("Enter name of student: ")
                                course1 = input("Enter the course: ")
                                contact1 = input("Enter contact no: ")
                                address1 = input("Enter the address: ")
                                gender1 = input("Enter M/F: ")
                                cur.execute("INSERT INTO students VALUES('"+name1+"','"+course1+"','"+contact1+"',\
                                '"+address1+"','"+gender1+"')")
                                cn.commit()
                                print("* SUCCESSFULLY ADDED *")
                                add_details()
                            elif c == 2:
                                print("---> Add Mentors <---")
                                name1 = input("Enter name of Mentor: ")
                                course1 = input("Enter the course: ")
                                cur.execute("INSERT INTO mentors VALUES('" + name1 + "','" + course1 + "')")
                                cn.commit()
                                print("* SUCCESSFULLY ADDED *")
                            elif c == 3:
                                print("BACK TO MAIN MENU")
                                main_menu1()
                            else:
                                print("Invalid Input")
                                add_details()
                        add_details()

                    # Delete details
                    elif ch1 == 3:
                        def delete_details():
                            print("""
                                    1. STUDENTS
                                    2. MENTORS
                                    3. STUDENT_USERS
                                    4. MENTOR_USERS
                                    5. GO BACK
                                                                """)
                            choice = int(input("Enter your Choice: "))
                            # Student Deletion
                            if choice == 1:
                                name2 = input("Enter student name to delete: ")
                                cur.execute("select * from students where name='" + name2 + "'")
                                record = cur.fetchall()
                                print(record)
                                x = input("CONFIRM!? (y/n): ")
                                if x == "y" or x == "Y":
                                    cur.execute("delete from students where name='" + name2 + "'")
                                    cn.commit()
                                    print("Student has been deleted successfully")
                                elif x == "n" or x == "N":
                                    print("Deletion cancelled")
                                else:
                                    print("Error in deletion....")
                                delete_details()
                            # Mentor Deletion
                            elif choice == 2:
                                name2 = input("Enter mentor name to delete: ")
                                cur.execute("select * from mentors where name='" + name2 + "'")
                                record = cur.fetchall()
                                print(record)
                                x = input("CONFIRM!? (y/n): ")
                                if x == "y" or x == "Y":
                                    cur.execute("delete from mentors where name='" + name2 + "'")
                                    cn.commit()
                                    print("Mentor has been deleted successfully")
                                elif x == "n" or x == "N":
                                    print("Deletion cancelled")
                                else:
                                    print("Error in deletion....")
                                delete_details()
                            # Removing Student User
                            elif choice == 3:
                                username = input("Enter student username to delete: ")
                                cur.execute("select * from student_reg where username='" + username + "'")
                                record = cur.fetchall()
                                print(record)
                                x = input("CONFIRM!? (y/n): ")
                                if x == "y" or x == "Y":
                                    cur.execute("delete from student_reg where username='" + username + "'")
                                    cn.commit()
                                    print("User has been deleted successfully")
                                elif x == "n" or x == "N":
                                    print("Deletion cancelled")
                                else:
                                    print("Error in deletion....")
                                delete_details()
                            # Removing mentor User
                            elif choice == 4:
                                username = input("Enter mentor username to delete: ")
                                cur.execute("select * from mentor_reg where username='" + username + "'")
                                record = cur.fetchall()
                                print(record)
                                x = input("CONFIRM!? (y/n): ")
                                if x == "y" or x == "Y":
                                    cur.execute("delete from mentor_reg where username='" + username + "'")
                                    cn.commit()
                                    print("User has been deleted successfully")
                                elif x == "n" or x == "N":
                                    print("Deletion cancelled")
                                else:
                                    print("Error in deletion....")
                                delete_details()
                            elif choice == 5:
                                print("BACK TO MAIN MENU")
                                main_menu1()
                            else:
                                print("Invalid Input..Returning to main menu!")
                                main_menu1()

                        delete_details()

                    # Edit Details
                    elif ch1 == 4:
                        def edit():
                            print("""
                                    1: Edit Student table
                                    2: Edit Mentor table
                                    3. Go back to main menu
                                                                """)
                            ed = int(input("Enter which table to edit: "))
                            if ed == 1:
                                def edit_std():
                                    print("""
                                            a. Name
                                            b. Course
                                            c. Contact
                                            d. Address
                                            e. Gender
                                            f. Go back
                                                                    """)
                                    c = input("Enter which detail to update: ")
                                    if c == "a":
                                        name1 = input("Enter current value: ")
                                        update1 = input("Enter new value: ")
                                        sql = "UPDATE students SET name=%s WHERE name = %s"
                                        cur.execute(sql, (update1, name1))
                                        cn.commit()
                                        print("Updated!!!")
                                        print("")
                                        print("**MENU**")
                                        edit_std()

                                    elif c == "b":
                                        course1 = input("Enter current value: ")
                                        update1 = input("Enter new value: ")
                                        sql = "UPDATE students SET course=%s WHERE course = %s"
                                        cur.execute(sql, (update1, course1))
                                        cn.commit()
                                        print("Updated!!!")
                                        print("")
                                        print("**MENU**")
                                        edit_std()

                                    elif c == "c":
                                        contact = input("Enter current value: ")
                                        update1 = input("Enter new value: ")
                                        sql = "UPDATE students SET contact=%s WHERE contact = %s"
                                        cur.execute(sql, (update1, contact))
                                        cn.commit()
                                        print("Updated!!!")
                                        print("")
                                        print("**MENU**")
                                        edit_std()

                                    elif c == "d":
                                        address = input("Enter current value: ")
                                        update1 = input("Enter new value: ")
                                        sql = "UPDATE students SET address=%s WHERE address = %s"
                                        cur.execute(sql, (update1, address))
                                        cn.commit()
                                        print("Updated!!!")
                                        print("")
                                        print("**MENU**")
                                        edit_std()

                                    elif c == "e":
                                        gender = input("Enter current value: ")
                                        update1 = input("Enter new value: ")
                                        sql = "UPDATE students SET gender=%s WHERE gender = %s"
                                        cur.execute(sql, (update1, gender))
                                        cn.commit()
                                        print("Updated!!!")
                                        print("")
                                        print("**MENU**")
                                        edit_std()

                                    elif c == "f":
                                        print("Going back to edit menu..")
                                        edit()

                                    else:
                                        print("Invalid choice!!..Choose again")
                                        edit_std()

                                edit_std()

                            elif ed == 2:
                                def edit_mnt():
                                    print("""
                                            a. Name
                                            b. Course
                                            c. Go back
                                                                    """)
                                    ch = input("Enter which detail to update: ")
                                    if ch == "a":
                                        name = input("Enter current value: ")
                                        update = input("Enter new value: ")
                                        sql_formula = "UPDATE mentors SET name=%s WHERE name = %s"
                                        cur.execute(sql_formula, (update, name))
                                        cn.commit()
                                        print("Updated!!!")
                                        print("")
                                        print("**MENU**")
                                        edit_mnt()

                                    elif ch == "b":
                                        course = input("Enter current value: ")
                                        update = input("Enter new value: ")
                                        sql_formula = "UPDATE mentors SET course=%s WHERE course = %s"
                                        cur.execute(sql_formula, (update, course))
                                        cn.commit()
                                        print("Updated!!!")
                                        print("Updated!!!")
                                        print("")
                                        print("**MENU**")
                                        edit_mnt()

                                    elif ch == "c":
                                        print("Going back to edit menu..")
                                        edit()

                                    else:
                                        print("Invalid choice!!..Choose again")
                                        edit_mnt()

                                edit_mnt()

                            elif ed == 3:
                                print("Returning to main menu..")
                                main_menu1()

                            else:
                                print("Invalid choice!!..Choose again")
                                edit()

                        edit()

                    elif ch1 == 5:
                        print(" ---> THANK YOU <--- ")
                        print("Logging Out!...")
                        login()

                    else:
                        print("Invalid choice! Returning to main menu..")
                        main_menu1()

                main_menu1()
            else:
                print("Password Incorrect, Please enter correct password.., Login Again!!")
                login()

    # STUDENT USER
    elif a == 2:
        print("""
                ==========================================================
                                  LOGIN AS STUDENT USER
                ==========================================================
                                                            """)
        usr = input("Username : ")
        psd = input("Password : ")
        cur.execute("select password from student_reg where username='" + usr + "'")
        rec = cur.fetchall()
        for i in rec:
            a = list(i)
            if a[0] == str(psd):
                def main_menu2():
                    print("""
                            1. VIEW STUDENT DETAILS
                            2. ASSIGNMENTS
                            3. LOGOUT
                                                        """)
                    ch2 = int(input("Enter your Choice: "))
                    if ch2 == 1:
                        cur.execute("SELECT * from students")
                        rec1 = cur.fetchall()
                        for row1 in rec1:
                            print(row1)
                        print("Returning to main menu")
                        main_menu2()
                    elif ch2 == 2:
                        def assignments():
                            print("""
                                    1. VIEW ASSIGNMENTS
                                    2. MAIN MENU
                                                            """)
                            b = int(input("Enter your choice: "))
                            if b == 1:
                                print("--> ASSIGNMENTS <--")
                                cur.execute("SELECT * from assignment")
                                rec2 = cur.fetchall()
                                for row2 in rec2:
                                    print(row2)
                                print("Returning to main menu")
                                assignments()
                            elif b == 2:
                                print("Returning to main menu")
                                main_menu2()
                            else:
                                print("Invalid Input! Returning to main menu..")
                                main_menu2()
                        assignments()
                    elif ch2 == 3:
                        print(" ---> THANK YOU <--- ")
                        print("Loging Out...")
                        login()
                    else:
                        print("Invalid choice! Returning to main menu..")
                        main_menu2()
                main_menu2()
            else:
                print("Password Incorrect, Please enter correct password.., Login Again!!")
                login()

    # MENTOR USER
    elif a == 3:
        print("""
                ==========================================================
                                  LOGIN AS MENTOR USER
                ==========================================================
                                                            """)
        usr = input("Username : ")
        psd = input("Password : ")
        cur.execute("select password from mentor_reg where username='" + usr + "'")
        rec = cur.fetchall()
        for i in rec:
            a = list(i)
            if a[0] == str(psd):
                def main_menu3():
                    print("""
                            1. VIEW STUDENT DETAILS
                            2. ASSIGN ASSIGNMENTS
                            3. VIEW ASSIGNMENTS TABLE
                            4. LOGOUT
                                                        """)
                    ch3 = int(input("Enter your Choice: "))

                    if ch3 == 1:
                        cur.execute("SELECT * from students")
                        rec1 = cur.fetchall()
                        for row1 in rec1:
                            print(row1)
                        print("Returning to main menu")
                        main_menu3()

                    elif ch3 == 2:
                        print("---> Add Assignments <---")
                        question = input("Enter the topic: ")
                        submit_date = input("Enter the submission date: ")
                        cur.execute("INSERT INTO assignment VALUES('" + question + "','" + submit_date + "')")
                        cn.commit()
                        print("* SUCCESSFULLY ADDED *")
                        print("Returning to main menu..")
                        main_menu3()

                    elif ch3 == 3:
                        cur.execute("SELECT * from assignment")
                        rec2 = cur.fetchall()
                        for d in rec2:
                            print(d)
                        print("Returning to main menu")
                        main_menu3()

                    elif ch3 == 4:
                        print(" ---> THANK YOU <--- ")
                        print("Loging Out...")
                        login()
                    else:
                        print("Invalid choice! Returning to main menu..")
                main_menu3()
            else:
                print("Password Incorrect, Please enter correct password.., Login Again!!")
                login()
    elif a == 4:
        print("BASIC MENU")
        signup()

    else:
        print("Invalid choice! Returning to main menu..")
        login()

    login()


basic_features()
