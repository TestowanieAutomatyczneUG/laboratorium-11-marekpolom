import unittest
from unittest.mock import *

from sample.friendships import FriendShips


class TestFriendships(unittest.TestCase):

    def test_make_friends(self):
        temp = FriendShips()
        temp.makeFriends("Kowalski", "Nowak")

        self.assertEqual(temp.data, {"Kowalski": ["Nowak"], "Nowak": ["Kowalski"]})

    def test_make_friends_2(self):
        temp = FriendShips()
        temp.makeFriends("Kowalski", "Nowak")
        temp.makeFriends("Kowalski", "Kwiatkowski")

        self.assertEqual(temp.data, {"Kowalski": ["Nowak", "Kwiatkowski"], "Nowak": ["Kowalski"], "Kwiatkowski": ["Kowalski"]})

    def test_make_friends_again(self):
        temp = FriendShips()
        temp.makeFriends("Kowalski", "Nowak")
        temp.makeFriends("Kowalski", "Nowak")

        self.assertEqual(temp.makeFriends("Kowalski", "Nowak"), 'Already friends!')

    def test_get_friends_list(self):
        temp = FriendShips()
        temp.makeFriends("Kowalski", "Nowak")

        self.assertEqual(temp.getFriendsList("Kowalski"), ["Nowak"])

    def test_get_friends_list_error(self):
        temp = FriendShips()
        temp.makeFriends("Kowalski", "Nowak")

        with self.assertRaises(KeyError): temp.getFriendsList("Kwiatkowski")

    def test_are_friends_true(self):
        temp = FriendShips()
        temp.makeFriends("Kowalski", "Nowak")
        temp.makeFriends("Kowalski", "Kwiatkowski")

        self.assertTrue(temp.areFriends("Kowalski", "Kwiatkowski"))

    def test_are_friends_false(self):
        temp = FriendShips()
        temp.makeFriends("Kowalski", "Nowak")
        temp.makeFriends("Kowalski", "Kwiatkowski")

        self.assertFalse(temp.areFriends("Nowak", "Kwiatkowski"))

    def test_are_friends_error(self):
        temp = FriendShips()
        temp.makeFriends("Kowalski", "Nowak")

        with self.assertRaises(KeyError): temp.areFriends("Kwiatkowski", "Kowalski")


if __name__ == '__main__':
    unittest.main()
