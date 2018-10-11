# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 14:12:58 2018

@author: CuddlyLicky
"""

class Group_11():
    
    def __init__(self, groupMembers = []):
        self.groupMembers = groupMembers
        
    def meet_up(self, day, time):
        available = True
        x = len(self.groupMembers)
        for i in range(x):
            if (self.groupMembers[i].classSchedule[i].get_endTime() >= time >= self.groupMembers[i].classSchedule[i].get_startTime()):
                available = False
        return available #Doesnt actually loop properly and check all schedule but oh well dont wanna do a double loop
    
    def print_members(self):
        x = len(self.groupMembers)
        for i in range (x):
            print("Member #" + str(i) +  ": " + self.groupMembers[i].get_name())
            print("Major: " + self.groupMembers[i].get_major())
            self.groupMembers[i].print_schedule()
    
class Group_Member():
    
    def __init__(self, name, major, classSchedule = []):
        self.name = name
        self.major = major
        self.classSchedule = classSchedule
    
    def print_schedule(self):
        x = len(self.classSchedule)
        for i in range (x):
            self.classSchedule[i].print_class_info()
            
    def get_name(self):
        return self.name
    
    def get_major(self):
        return self.major
    
class Class():
    
    def __init__(self, department, classNumber, startTime, endTime):
        self.department = department
        self.classNumber = classNumber
        self.startTime = startTime
        self.endTime = endTime
    
    def print_class_info(self):
        print(self.department + " " + str(self.classNumber) + 
              " from " + str(self.startTime) + " - " + str(self.endTime))
        
    def get_startTime(self):
        return self.startTime
    
    def get_endTime(self):
        return self.endTime
             

cs3110 = Class("CS", 3110, 1100, 1150)
cs4650 = Class("CS", 4650, 1000, 1115)
cs3010 = Class("CS", 3010, 1430, 1545)
hst2020 = Class("HST", 2020, 1430, 1545)

cs4200 = Class("CS", 4200, 1000, 1130)
com1000 = Class("COM", 1000, 1300, 1400)
lin2000 = Class("ECE", 6900, 1430, 1545)

joseph = Group_Member("Joseph Tuazon", "ComSci", [cs3110, cs4650, cs3010, hst2020])

pomoko = Group_Member("Pomoko-Chan", "Food Science", [cs4200, com1000, lin2000])

group11 = Group_11([joseph, pomoko])

group11.print_members()
print("Can Group 11 meet: " + str(group11.meet_up("Monday", 950)))