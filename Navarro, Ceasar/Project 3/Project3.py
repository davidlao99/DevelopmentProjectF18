class Group_16:

    def __init__(self):
        self.time = ""
        self.days = ""
        self.names = ["Eric", "Michael", "Ceasar"]

    def Meet_up(self,t,d):
        print("Can meet" + str(self.time) + str(self.days))

    def Print_Members(self):
        print(self.names)




class GroupMembers:
    def __init__(self,name,major,classSchdule):
        name = ""
        major = 0
        classSchdule = classSchdule.append[classSchdule]
        self.name = name
        self.major = major
        self.classSchdule = classSchdule

    
    def PrintClassInfo(self):
        x = len(self.classSchdule)
        for i in range(x):
            print(self.classSchdule[i])

class Class:
    def __init__(self,department ,classNumber,startTime,endTime):
        self.department = department
        self.classNumber = classNumber
        self.startTime = startTime
        self.endTime = endTime
    
    def PrintClassInfo(self):
        print("h")