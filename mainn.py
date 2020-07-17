import sys
import csv
import os
from datetime import date, timedelta

class ITAcademy:
    PhoneNo = 0
    name = ''
    address=''
    email=''
    deposit = 0


    def Account(self):
        self.PhoneNo = int(input("Enter the phone no for registration : "))
        self.name = input("Enter the your name : ")
        self.address = input("Enter your current address: ")
        self.email = input("Enter the Student Email : ")
        self.deposit = int(input("Enter The amount you want to Register ( 20000 or 10000 )"))
        with open('student_info.txt', 'a', newline= '') as studentfile:
            studentfileWriter = csv.writer(studentfile)
            if self.deposit >= 10000:
                studentfileWriter.writerow(
                    [self.PhoneNo, self.name, self.address, self.email, self.deposit])
                studentfile.close()

            else:

                if self.deposit<=10000:
                    dt = date.today() + timedelta(10)
                    print("Please pay the remaining amount by date:", dt)
                    studentfileWriter.writerow(
                        [self.PhoneNo, self.name, self.address, self.email, self.deposit])
                    print("Record has been written to file")
                    studentfile.close()






def show_courses():
    print("\n")
    print(" Here  is the details of our course list")
    text_file = open('course.txt', 'r')
    line_list = text_file.read();
    print(line_list)
    print("THE COURSE OF OUR ACADEMY ")
    text_file.close()

def studentdetails():

    # Open the file for reading
    f = open("student_info.txt", "r", encoding="utf8")
    displaylist = csv.reader(f)
    dt = date.today() + timedelta(10)
    for i in displaylist:
        print("\n")
        print(i)
        balance= int(i[4])
        print("Total Balance in your account for Registration is :", balance)
        if balance>=20000:
            remaining_balance = balance-20000
            print("you can withdraw the money after complition of course")
            print("Remaining Balance to be receive after the Regitration is :", remaining_balance)
        else:
            due= 20000-balance
            print("Amount {} still needed to be paid for the Registration by date {}". format(due, dt))

    #print(displaylist)
    f.close()

def modifydetails():

    num=input("enter the phone number of student to be updated")
    with open('sudent_info.txt', 'r+',newline='') as f:
        ro=csv.reader(f)
        rows=[]
        for rec in ro:
            rows.append(rec)
        for i in range(len(rows)):
            if rows[i][0]== num:
                rows[i][1]=input("enter a new name")
                rows[i][2] = input("enter a address")
                rows[i][3] = input("enter a email")
                rows[i][4] = int(input("enter a deposit"))

    print(rows)
    with open('info.txt', 'w', newline='') as f:
        wo=csv.writer(f)
        wo.writerows(rows)
    f.close()

def deletedetails():
    num=input("Enter the pphone number of a student that is to be deleted")
    with open('student_info.txt', 'r+',newline='') as f:
        one=csv.reader(f)
        rows=[]
        os=[]
        for rec in one:
            rows.append(rec)
        for i in range(len(rows)):
            if rows[i][0]!=num:
                os.append(rows[i])
        #print(sows)
        print("*********Your account has been deleted permanently, SORRY!!!!!!********")

    with open('student_info.txt', 'w', newline='') as f:
        sm=csv.writer(f)
        sm.writerows(sows)
    f.close()


def menu():
    datetoday=date.today()

    dash = '-' * 40

    print(dash)
    print('\t''\t''Welcome to Kenjal IT Academy ')
    print(dash)
    print(' Date of Today :', datetoday)
    print("\n")


    choice = input(
        """1. Enter Course study  details
        2. Enter Student details here!!
        3. View student details.
        4. Modify students details.5. Delete students details.6. Quit.
        Please enter your choice: """)

    if choice == '1':
        show_courses()
    elif choice=='2':
        student = ITAcademy()
        student.Account()
    elif choice == '3':
        studentdetails()
    elif choice == '4':
        modifydetails()
    elif choice == '5':
        deletedetails()
    elif choice == '6':
        sys.exit()
    else:
        print("You must only select one  option")
        print("Please try again")
        menu()
menu()



