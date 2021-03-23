class AssignmentClass:
    def __init__(self,firstname,lastname,emailid):
        self.firstname=firstname
        print("firstname",firstname)
        self.lastname=lastname
        print("lastname",lastname)
        self.emailid=emailid
        print("emailid",emailid)


    def get_marks(self,mark1,mark2,mark3):
        self.mark1=mark1
        print("mark1",mark1)
        self.mark2=mark2
        print("mark2",mark2)
        self.mark3=mark3
        print("mark3",mark3)

    def total(self):
        self.total=self.mark1+self.mark2+self.mark3
        print("total",self.total)

    def average(self):
        average = (self.total)/3
        print("average",average)

