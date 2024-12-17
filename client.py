from task import task
from teamMember import teamMember

task1 = task('1')
task2 = task('2')

member1 = teamMember('a')
member2 = teamMember('b')
member3 = teamMember('c')

task1.addMember(member1)
task1.addMember(member2)
task2.addMember(member3)
task2.addMember(member2)
task2.addMember(member3)

task1.subjectState = "Faster"
task2.subjectState = 5

print(f"\n{member1.name} is working on: {member1.task.name} with state: \"{member1.memberState}\"")
print(f"{member2.name} is working on: {member2.task.name} with state: \"{member2.memberState}\"")
print(f"{member3.name} is working on: {member3.task.name} with state: {member3.memberState}")


