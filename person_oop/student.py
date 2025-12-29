

class student:

    def __init__(self,first_name,last_name="Doe"):
        self.first_name = first_name
        self.last_name = last_name

    def get_avarage_score(self,grades):
        sum = 0
        for grade in grades:
            sum = sum+grade

        avg=sum / len(grades)
        print(F"the avrage score is {avg}")
        return avg
    def compare_avarage(self):
        if avg1 >avg2:
            print("avg1 is higher than avg2 ")

        else :
            print("avg2 is higher than avg1 ")

