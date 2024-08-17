class Studentss():
    def __init__(self, capacity):
        self.capacity=capacity
        self.students=[]

    def add_students(self, name):
        if not self.open_seats():
            return False
        self.students.append(name)
        return True
    def open_seats(self):
        return self.capacity - len(self.students)
    
s = Studentss(3)
v = ["jalal","Aifa","Jahin","Dolon"]
for student in v:
    if s.add_students(student):
        print(f'{student} added to this year student list.')
    else:
        print('all seates are allocated.')
