class group_5():
    def __init__(self,groupmembers):
        self.groupmembers = groupmembers

    def meet_up(self, day, time):
        self.day = day
        self.time = time
		
    def print_members(self):
        print(self.groupmembers)

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
        print(self.department + " " + str(self.classNumber) + " "  + str(self.startTime) + " to " + str(self.endTime) + " " + self.meetingDays)



