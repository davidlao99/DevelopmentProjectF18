import json


class Group_16:
    def __init__(self, members):
        self.members = members

    def meet_up(self, day, time):
        pass

    def print_members(self):
        pass

    def __repr__(self):
        return f'Group_16({self.members})'


class GroupMember:
    def __init__(self, name, major, classSchedule):
        self.name = name
        self.major = major
        self.classSchedule = classSchedule

    def print_schedule(self):
        pass

    def __repr__(self):
        return f'GroupMember({self.name}, {self.major}, {self.classSchedule})'


class Class:
    def __init__(self, department, classNumber, weekdays,  startTime, endTime):
        self.department = department
        self.classNumber = classNumber
        self.weekdays = weekdays
        self.startTime = startTime
        self.endTime = endTime

    def __repr__(self):
        return (f"Class({self.department}, "
                f"{self.classNumber}, "
                f"{self.weekdays}, "
                f"{self.startTime}, "
                f"{self.endTime})")


# The loadMembers() creates and returns an instance of Group_16.
# It creates a list of GroupMember() from the information found in the
# members.json file. That list is then passed to a new instance of Group_16


def loadMembers():
    with open('members.json', 'r') as read_file:
        members = []
        data = json.load(read_file)
        for x in data:
            classes = [loadClass(y) for y in x['classes']]
            members.append(GroupMember(x['name'], x['major'], classes))
    return Group_16(members)


# This function takes a classNumber to be used as a key for the JSON file
# It loads the json file containing said class information and passes it to a
# new instance of Class.
# That instance is then returned.


def loadClass(entry):
    with open('classes.json', 'r') as read_file:
        data = json.load(read_file)[entry]
        item = Class(data['department'],
                     entry,
                     data['weekdays'],
                     data['start'],
                     data['end'])
    return item


if __name__ == '__main__':
    data = loadMembers()
