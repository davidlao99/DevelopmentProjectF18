class Group_2():
    groupMembers = ['Lam Lieu', 'Neha Jayan', 'Marlon Aquino', 'David Lao'];
    def meet_up(self, day, time):
        print('hello')
    def print_members(self):

class GroupMember():
    def __init__(self, name, major, classSchdule):
        self.name = name
        self.major = major
        self.classSchedule = classSchdule

class Class():
    def __init__(self, department, classNumber, startTime, endTime):
        self.department = department
        self.classNumber = classNumber
        self.startTime = startTime
        self.endTime = endTime

    def print_class_info(self):
        print('Department: ' + self.department)
        print('Class Number: ' + self.classNumber)
        print('Start Time: ' + self.startTime)
        print('End Time: ' + self.endTime)