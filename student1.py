class Student:
    def __init__(self, name, gender, age, score):
        self.name = name
        self.gender = gender
        self.age = int(age)
        self.score = int(score)
        self.make_grade()

    def make_grade(self):
        grades = ['A', 'B', 'C', 'D', 'E', 'F']
        if self.score == 100:
            self.grade = 'A+'
        else:
            self.grade = grades[9 - self.score // 10]

    def __str__(self):
        return "{}**\t{}\t{}\t{}\t{}".format(self.name[0], self.gender, self.age, self.score, self.grade)

students = []
with open('students.csv', 'r', encoding='utf8') as file:
    for i, line in enumerate(file):
        if i == 0: continue
        name, gender, age, score = line.strip().split(',')
        students.append(Student(name, gender, age, score))

students.sort(key = lambda stu: stu.score, reverse=True)

print('성명\t성별\t나이\t성적\t학점')
print('----\t----\t----\t----\t----')
for s in students:
    print(s)

from functools import reduce
total = reduce(lambda x, y: x + y.score, students, 0)
print('----\t----\t----\t----\t----')
print(f"\t전체 성적>>>\t{total}")