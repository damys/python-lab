# __repr__()用于显示给开发人员, 而__str__()用于显示给用户

class Person(object):
     
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
 
class Student(Person):
 
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
 
    def __str__(self):
        return '(Person: %s, %s, %s)' % (self.name, self.gender, self.score)
 
s = Student('json', 'male', 95)
print(s)
 
(Person: json, male, 95)
