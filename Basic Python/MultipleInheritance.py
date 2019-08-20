class A:
    id =1
    def say_hi(self):
        print("A")
class B:
    id=2
    def say_hi(self):
        print("B")
class C:
    id=3
    def say_hi(self):
        print("C")
class M(C,A,B):
    pass

print(M.id)
M.say_hi()


