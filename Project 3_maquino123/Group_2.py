from GroupMember import GroupMember
from Class import Class
class Group_2:


    Class_Marlon = Class("CS", "2400", 5.00, 6.00)
    GroupMember_Marlon = GroupMember("Marlon", "Computer Science", Class_Marlon.print_class_info())
    Group_2_Marlon = GroupMember_Marlon.print_schedule()

    memberslist = [Group_2_Marlon]

    for m in memberslist:
        print(m)