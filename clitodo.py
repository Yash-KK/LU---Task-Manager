import sqBase
import os

os.system("cls")
ch = int(input("Choose What You Want? \n\t1. View Task\n\t2. Add A Task\n\t3. Delete A Task\n\t4.QUIT\n\t>"))

while ch != 4:
    if ch ==1:
        os.system("cls")
        print("ID" + "\t" + "TASK\n")
        for rows in sqBase.show():
            print(str(rows[0]) + "\t" + rows[1])
        ch = int(input("Choose What You Want? \n\t1. View Task\n\t2. Add A Task\n\t3. Delete A Task\n\t4.QUIT\n\t>"))
    elif ch ==2:
        task = input("Enter A Task: ")
        if(len(task) != 0):
            sqBase.insertData(task)
        ch = int(input("Choose What You Want? \n\t1. View Task\n\t2. Add A Task\n\t3. Delete A Task\n\t4.QUIT\n\t>"))
    
    elif ch == 3:
        os.system("cls")
        print("ID" + '\t' + "TASK\n")
        for rows in sqBase.show():
            print(str(rows[0]) + '\t' + rows[1])
        id = int(input("Choose a Task To delete: "))
        sqBase.deleteById(id)
        ch = int(input("Choose What You Want? \n\t1. View Task\n\t2. Add A Task\n\t3. Delete A Task\n\t4.QUIT\n\t>"))
    else:
        os.system("cls")
        print("Choose a Valid Number")
        ch = int(input("Choose What You Want? \n\t1. View Task\n\t2. Add A Task\n\t3. Delete A Task\n\t4.QUIT\n\t>"))
else:
    os.system("cls")
    print("Thank you for Using The Application")