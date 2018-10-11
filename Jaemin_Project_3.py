class Group_6:

    def __init__(self):
        self.time = ""
        self.day = ""
        self.names = ["Jaemin", "Jose", "Kobe", "Wilson"]

    def meet_up(self, time, day):
        print("Group members can meet " + str(self.time) + str(self.day))

    def print_members(self):
        print(self.names)


class GroupMember:
    def __init__(self, name, major, class_schedule):
        self.name = name
        self.major = major
        self.class_schedule = class_schedule
        class_schedule = class_schedule.append[class_schedule]

    def print(self):
        x = len(self.class_schedule)
        for i in range(x):
            print(self.class_schedule[i])


class Class:
    def __init__ (self, department, class_number, start_time, end_time):
        self.department = department
        self.classNumber = class_number
        self.startTime = start_time
        self.endTime = end_time

    def print_class_info(self):
        print("Department: " + Class.department)
        print("Class number: " + Class.classNumber)
        print("Start time: " + Class.startTime)
        print("End time: " + Class.endTime)
