import unittest

from app.modules.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("John", "rock")

    def test_player_has_name(self):
        self.assertEqual("John", self.player.name)

    def test_player_has_choice(self):
        self.assertEqual("rock", self.player.choice)