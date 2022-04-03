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


from functools import reduce

def my_add(x, y):
    return x + y.score

ttt = reduce(my_add, students, 0)
ttt1 = reduce(lambda x, y: x+y.score, students, 0)

print(ttt1)