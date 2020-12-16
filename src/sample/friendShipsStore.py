from sample.friendships import FriendShips

class FriendShipsStore:
    def __init__(self):
        self.friendShips = FriendShips()

    def makeFriends(self, person1, person2):
        self.friendShips.makeFriends(person1, person2)

    def getFriendsList(self, person):
        self.friendShips.getFriendsList(person)

    def areFriends(self, person1, person2):
        self.friendShips.areFriends(person1, person2)

    def addFriend(self, person, friend):
        self.friendShips.addFriend(person, friend)