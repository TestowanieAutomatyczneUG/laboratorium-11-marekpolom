import unittest
from unittest.mock import *
from unittest.mock import MagicMock

from sample.friendShipsStore import FriendShipsStore


class TestFriendships(unittest.TestCase):
    def setUp(self):
        self.temp = FriendShipsStore()

    def test_make_friends(self):
        self.temp.friendShips = MagicMock()
        self.temp.makeFriends("Kowalski", "Nowak")

        self.temp.friendShips.makeFriends.assert_called_with("Kowalski", "Nowak")

    def test_get_friends_list(self):
        self.temp.friendShips = MagicMock()
        self.temp.makeFriends("Kowalski", "Nowak")
        self.temp.getFriendsList("Kowalski")

        self.temp.friendShips.getFriendsList.assert_called_with("Kowalski")

    def test_get_friends_list_error(self):
        self.temp.friendShips.getFriendsList = MagicMock(side_effect=KeyError)
        self.temp.makeFriends("Kowalski", "Nowak")

        with self.assertRaises(KeyError): self.temp.getFriendsList("Kwiatkowski")

        self.temp.friendShips.getFriendsList.assert_called_with("Kwiatkowski")

    def test_are_friends_true(self):
        self.temp.friendShips = MagicMock()

        self.temp.makeFriends("Kowalski", "Nowak")
        self.temp.areFriends("Kowalski", "Nowak")

        self.temp.friendShips.areFriends.assert_called_with("Kowalski", "Nowak")

    def test_are_friends_false(self):
        self.temp.friendShips = MagicMock()

        self.temp.makeFriends("Kowalski", "Nowak")
        self.temp.makeFriends("Kowalski", "Kwiatkowski")

        self.temp.areFriends("Nowak", "Kwiatkowski")

        self.temp.friendShips.areFriends.assert_called_with("Nowak", "Kwiatkowski")

    def test_are_friends_error(self):
        self.temp.friendShips.areFriends = MagicMock(side_effect=KeyError)
        self.temp.makeFriends("Kowalski", "Nowak")

        with self.assertRaises(KeyError): self.temp.areFriends("Kwiatkowski", "Kowalski")

        self.temp.friendShips.areFriends.assert_called_with("Kwiatkowski", "Kowalski")


if __name__ == '__main__':
    unittest.main()
