class Class:

    def __init__(self, department, classNumber, startTime, endTime):
        self.department = department
        self.classNumber = classNumber
        self.startTime = str(startTime)
        self.endTime = str(endTime)


    #We could probably format the time to make it look like an actual time
    def print_class_info(self):
        return str("\nDepartment: " + self.department + "\nClass Number: " + self.classNumber + "\nStart Time: " + self.startTime + "\nEnd Time: " + self.endTime)




