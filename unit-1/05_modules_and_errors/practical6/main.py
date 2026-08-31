from student import get_student_data,get_student_total
from report import get_student_report

std_data=get_student_data()
student_total=get_student_total(std_data)
print(std_data)
report_data=get_student_report(std_data)
# print(report_data)