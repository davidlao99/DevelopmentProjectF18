class Group_16:

    def __init__(self, members):
        self.members = members
 
    def print_member_info(self):
        for member in self.members
        member.print_schedule()

class GroupMember:

    def __init__(self, name, major, classSchedule):

        self.classSchedule = classSchedule
        self.name = name
        self.major = major
        
    def print_schedule(self):

        i=1

        for startTime in self.classSchedule:
            print(self.major + " " + str(i))
            startTime.print_class_info()
            i += 1
            
class Class:
    
    def __init__(self, department, day, classNumber, startTime, endTime):
        self.department = department
        self.day = day
        self.classNumber = classNumber
        self.startTime = startTime
        self.endTime = endTime

    def print_class_info(self):
        print("Department: " + self.department + "\nClassNumber: " + str(self.classNumber) +
              "\nStartTime: "  + self.startTime + "\nEndTime: " + self.endTime)

