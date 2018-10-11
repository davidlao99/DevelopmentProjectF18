class Group2:
    def meet_up(self, day, time):
        self.day = day
        self.time = time
    def print_members(self):

class GroupMember:
    def __init__(self, name, major, classSchdule):
        self.name = name
        self.major = major
        self.classSchedule = classSchdule
    def print_schedule(self):
        for
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
