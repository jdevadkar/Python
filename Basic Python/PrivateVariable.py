class PrivateVariable:
    __hiddenVariable =0

    def __init__(self, hiddenVariable):
        self.__hiddenVariable=hiddenVariable
    def display(self):
        print("hiddenVariable :", self.__hiddenVariable)
p=PrivateVariable(12)
p.display()

print("HiddenVariable :", __hiddenVariable)