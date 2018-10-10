from Class import Class
class GroupMember(Class):

    def __init__(self, name, major, classSchedule = []):
        self.name = name
        self.major = major
        self.classSchedule = classSchedule

    def print_schedule(self):
        return str("Name: " + self.name + "\nMajor: " + self.major + "\n*** Class Schedule ***" + self.classSchedule)
