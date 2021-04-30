import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writter = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writter.writerow(["Name", "Age", "Condact Number", "E-mail ID"])


        writter.writerow(info_list)
if __name__ == '__main__':
    condition = True
    stu_no = 1
    while(condition):
        student_info = input(f"Enter the information of student({stu_no}) in the format of (Name Age Condact_Number E-mail_ID) : ")

        student_info_list = student_info.split(' ')
        print(f"\nThe entered info is -\nName : {student_info_list[0]}\nAge: {student_info_list[1]}"
             f"\nCondact Number: {student_info_list[2]}\nE-mail ID: {student_info_list[3]}")
        check = input("is the entered info is correct ? (y/n)")
        if check == "y":
            write_into_csv(student_info_list)

            condition_check = input("Enter (y/n) if you want to enter information for new student : ")
            if condition_check == "y":
                condition = True
                stu_no += 1
            elif condition_check == "n":
                condition = False
        elif check == "n":
            print("\nPlease re-enter the value!")