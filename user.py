class User:
    def __init__(self):
        self.username = "user1"

    def changeName(self, other):
        if(not isinstance(other, str)):
            raise TypeError
        self.username = other

    def getName(self):
        return self.username
