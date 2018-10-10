class group_Number():
    def __init__(self,groupnumber, day, time):
        self.groupnumber = groupnumber
        self.day = day
        self.time = time
    def meet_up(self, day, time):

    def print_members(self):
        print(str(self.groupnumber) + "Group members: " + )

class groupMember():
    def __init__(self, name, major, classSchdule):
        self.name = name
        self.major = major
        self.classSchdule = classSchdule

class Class():
    def __init__(self, department, classNumber, startTime, endTime, meetingDays):
        self.department = department
        self.classNumber = classNumber
        self.startTime = startTime
        self.endTime = endTime
        self.meetingDays = meetingDays
    def print_class_info(self):
        print(self.department + " " + str(self.classNumber) + " "  + str(self.startTime) + " " + str(self.endTime) + " " + self.meetingDays)



c1 = Class("ECE", 1000, 1.00, 2.30, "Monday Wednesday")
c1.print_class_info()

