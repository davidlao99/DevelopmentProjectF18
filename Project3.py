class group_5():
    def __init__(self,groupMembers):
        self.groupMembers = groupMembers

    def meet_up(self, day, time):
        meet = True
        for member in self.groupMembers:
            for classes in member.classSchdule:
                for meetdays in classes.meetingDays:
                    if (meetdays == day):
                        if (classes.startTime <= time and classes.endTime >= time):  # Can't meet up that day
                            meet = False
                            print( "We can't meet up on " + str(day) + " at " + str(time))
        if(meet == True):
            print("We can meet on " + str(day) + " at " + str(time))

    def print_members(self):
        for member in self.groupMembers:
            print("Member: " + member.name + ", Major: " + member.major + ", Schedule: ")
            member.print_schedule()

class groupMember():
    def __init__(self, name, major, classSchdule):
        self.name = name
        self.major = major
        self.classSchdule = classSchdule

    def print_schedule(self):
        i= 0
        for i in range(len(self.classSchdule)):
            self.classSchdule[i].print_class_info()

class Class():
    def __init__(self, department, classNumber, startTime, endTime, meetingDays):
        self.department = department
        self.classNumber = classNumber
        self.startTime = startTime
        self.endTime = endTime
        self.meetingDays = meetingDays

    def print_class_info(self):
        print(self.department + " " + str(self.classNumber) + " " + str(self.startTime) + " to " + str(self.endTime) + " on " + str(self.meetingDays) + " ")

digitallogic = Class("ECE", 2300, 14.30, 15.45, ["Monday", "Wednesday"])
circuitanalysis = Class("ECE", 2101, 11.30, 12.45, ["Monday", "Wednesday"])
microelectronics = Class("ECE", 2200, 16.00, 17.15, ["Monday", "Wednesday"])
digitallogiclab = Class("ECE", "2300L", 16, 19, ["Thursday"])
circuitlab = Class("ECE", "2101L", 16, 19, ["Tuesday"])
photography = Class("COM", 2280, 14.30, 15.45, ["Tuesday", "Thursday"])

schedule1 = [digitallogic, circuitanalysis, microelectronics,digitallogiclab, circuitlab, photography]

keith = groupMember("Keith", "ECE", schedule1)

group = group_5([keith])
group.print_members()
group.meet_up("Monday", 15)
