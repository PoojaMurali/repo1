class Student:
    def __init__(self, first_name, last_name, email_id):
        self.first_name = first_name
        self.last_name = last_name
        self.email_id = email_id

    def get_student_details(self):
        return self.first_name,self.last_name,self.email_id

    def get_marks(self, mark1, mark2, mark3):
        self.mark1 = int(mark1)
        self.mark2 = int(mark2)
        self.mark3 = int(mark3)
        return self.mark1,self.mark2,self.mark3


    def get_total(self):
        self.total = self.mark1 + self.mark2 + self.mark3
        return self.total

    def get_average(self):
        self.average = (self.total) / 3
        return self.average