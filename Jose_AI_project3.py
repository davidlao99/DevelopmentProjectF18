#Jose Garcia
#AI_Project3

class Class:
    def information(member, depart, classNum, day, start, end):
        member.depart = depart
        member.classNum = classNum
        member.day = day
        member.start = start
        member.end = end

    def printInfo(member):
        print("Department: " + str(member.depart))
        print("Class Number: " + str(member.classNum))
        print("Day: " + str(member.day))
        print("Start: " + str(member.start))
        print("End: " + str(member.end))

class TeamMember(Class):

    def teamInfo(member, name, major, schedule = []):
        member.name = name
        member.major = major
        member.schedule = schedule

    def printTeam(member):
        print("Name: " + str(self.name))
        print("major: " + str(self.major))
        print("Class Schedule")
        i = 0
        for i in range (len(member.schedule)):
            member.schedule[c].print_class_info()
#main class to print information
class main:
    ProgLang = Class("CS", "4080", "MWF", 12:00, 12:50)
    Jschedule = [ProgLang]
    member2 = Class("CS", "3650", "TT", 1:00, 2:00)
    mem2schedule = [member2]
    member3 = Class("CS", "4800", "MW", 9:00, 10:00)
    mem3schedule = [member3]
    member4 = Class("CS", "2700", "TT", 8:00, 8:50)
    mem4schedule = [member4]

    teamList[Jschedule, member2, member3, member4]

    def information(member, members):
        member.teamList = members

    def printInfo(member):
        print(member.teamList

    for TeamMember in teamList:
        TeamMember.printTeam()
