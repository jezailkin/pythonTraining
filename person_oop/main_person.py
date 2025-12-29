from person_oop.driver import driver
from person_oop.person import person
from person_oop.student import student

student_1 = student(first_name="John", last_name="Smith")
student_2 = student(first_name="Mike", last_name="Doe")
student_3 = student("Johny")

avg1 = student_1.get_avarage_score([77,50,90,88,100])
avg2 = student_2.get_avarage_score([75,50,90,78,99])


if avg1 > avg2:
    print("Student 1 is better than Student 2")

else:
    print("Student 2 is better than Student 1")

person_1=person(name="John", age=18)
person_2=person(name="Mike", age=20)
person_3=person(name="Johny", age=17)

person_1.age_calculator(18)
person_2.age_calculator(20)
person_3.age_calculator(17)


driver_1= driver(license_level=2)
driver_2= driver(license_level=3)

driver_1.get_license_level()
driver_2.get_license_level()