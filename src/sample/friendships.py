class FriendShips:
    def __init__(self):
        self.data = {}

    def makeFriends(self, person1, person2):
        if person1 in self.data.keys():
            if person2 in self.data[person1]:
                return 'Already friends!'
            else:
                self.addFriend(person1, person2)
                self.addFriend(person2, person1)
        else:
            self.addFriend(person1, person2)
            self.addFriend(person2, person1)

    def getFriendsList(self, person):
        try:
            return self.data[person]
        except KeyError:
            raise KeyError

    def areFriends(self, person1, person2):
        try:
            return person2 in self.data[person1]
        except KeyError:
            raise KeyError

    def addFriend(self, person, friend):
        try:
            if not person in self.data.keys():
                self.data[person] = []

            self.data[person].append(friend)
        except KeyError:
            raise KeyError