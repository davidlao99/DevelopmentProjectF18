from Group5 import Group5
from GroupMember import GroupMember
from Class import Class

a = []
a = a + [Class('MATH', 1, 12.00, 13.00, ["Monday", "Tuesday"])]
a = a + [Class('ENGLISH', 1, 14.00, 15.00, ["Monday", "Wednesday"])]
a = a + [Class('PHYSICS', 1, 10.00, 12.00, ["Tuesday", "Thursday"])]

caitlin = GroupMember("Caitlin", "Electrical Engineering", a[0:2])
tangy = GroupMember("Jonathan", "Biology", a[1:3])

my_group = Group5([caitlin, tangy])