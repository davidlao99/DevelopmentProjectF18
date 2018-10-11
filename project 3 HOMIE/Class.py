class Class():
    def __init__(self, department, class_number, start_time, end_time, meeting_days):
        self.department = department
        self.class_number = class_number
        self.start_time = start_time
        self.end_time = end_time
        self.meeting_days = meeting_days

    def print_class_info(self):
        print(f"{self.department:<8} {self.class_number:<6} {self.start_time:<6} {self.end_time:<4} {self.meeting_days}")