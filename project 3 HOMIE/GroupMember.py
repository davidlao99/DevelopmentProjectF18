class GroupMember():
    def __init__(self, name, major, class_schedule):
        self.name = name
        self.major = major
        self.class_schedule = class_schedule

    def print_schedule(self):
        for _class in self.class_schedule:
            _class.print_class_info()