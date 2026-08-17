

def get_student_data():
    student_data=[]
    for i in range(2):
        name=input("enter your name")
        roll_no=int(input("enter your roll no"))
        marks1=int(input("enter marks1"))
        marks2=int(input("enter marks1"))
        std_dict={
            "name":name,
            "roll_no":roll_no,
            "marks1":marks1,
            "marks2":marks2,
        }
        student_data.append(std_dict)
    return student_data