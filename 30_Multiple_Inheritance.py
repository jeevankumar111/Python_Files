class Teacher:
    def teachers_action(self):
        print("I can teach")

class Engineer:
    def Engineers_action(self):
        print("I can code")

class Youtuber:
    def youtubers_action(self):
        print("I can code and teach")

class person(Teacher,Engineer,Youtuber):
    pass

coder = person()
coder.teachers_action()
coder.Engineers_action()
coder.youtubers_action()