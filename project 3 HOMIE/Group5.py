class Group5():
    def __init__(self, member_list):
        self.member_list = member_list

    def meet_up(self, day, time):
        for member in self.member_list:
            for _class in member.class_schedule:
                if day in _class.meeting_days and _class.start_time <= time and time <= _class.end_time:
                    print(f"{member.name} has a class at that time.")
                    return

        # If the program makes it through the for loop, there are no conflicts
        print(f"No one has class at that time.")

    def print_members(self):
        for member in self.member_list:
            print(f"{member.name}\nMajor: {member.major}\nSchedule:")
            print(f"{'Dept':<8} {'Class':<6} {'Start':<6} {'End':<4} Days")
            member.print_schedule()