
class Group2:
    def meet_up(self, day, time):

    def print_members(self):

class GroupMember:
    def __init__(self, name, major, classSchedule):
        self.name = name
        self.major = major
        self.classSchedule = classSchedule
    def print_schedule(self):
        print("Name: " + str(self.name) + "\nMajor: " + str(self.major))
        print("*** Class Schedule ***")

        for i in range(len(self.classSchedule)):
            print(self.classSchedule[i].print_class_info)

class Class:
    def __init__(self, department, classNumber, startTime, endTime, meetingDays):
        self.department = department
        self.classNumber = classNumber
        self.startTime = startTime
        self.endTime = endTime
        self.meetingDays = meetingDays

    def print_class_info(self):
        print('Department: ' + self.department)
        print('Class Number: ' + self.classNumber)
        print('Start Time: ' + self.startTime)
        print('End Time: ' + self.endTime)
        for days in enumerate(meetingDays):
            print(days)

def lam_schedule():
    schedule = Class("CS", "2400", 10.45, 11.50, "M/W/F")
    return schedule

def group_member_lam():
    Lam = GroupMember("Lam Lieu", "Computer Science", lam_schedule())
    return Lam

def all_group_members():
    groupMembers = [group_member_lam()]
    return groupMembers

