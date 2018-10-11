class Group_7():
    GroupMembers = ["Jessica", "Sandra"]
    def meet_up(self, day, time):

    def print_members(self):


class GroupMember():
    def __init__(self, name, major, classSchdule):
        self.name = name
        self.major = major
        self.classSchdule = classSchdule

    def print_schedule(self):
        print (classSchdule)

class Class():
    def __init__(self, department, classNumber, startTime, endTime, meetingDays):
        self.department = department
        self.classNumber = classNumber
        self.startTime = startTime
        self.endTime = endTime
        self.meetingDays = meetingDays

    def print_class_info():
        print ("Department: " + self.department)
        print ("Class Number: " + self.classNumber)
        print ("Start Time: " + self.startTime)
        print ("End Time: " + self.endTime)
        print ("Meeting Days: " + self.meetingDays)
