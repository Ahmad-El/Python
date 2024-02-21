from collections import Counter
from players import *
import unittest


class Game(object):

    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1=None, player2=None):
        if player1 is None or player2 is None:
            self.default_toornament()
            return
        for _ in range(self.matches):
            player1_bet = player1.make_bet()
            player2_bet = player2.make_bet()
            player1.update_score(player2_bet)
            player2.update_score(player1_bet)
        self.registry.update({player1.name: player1.score})
        self.registry.update({player2.name: player2.score})
        scores = (player1.score, player2.score)
        player1.reset()
        player2.reset()
        return scores

    def top3(self):
        top = self.registry.most_common()
        for item in top:
            print(f'{item[0]} {item[1]}')
        return tuple(top)

    def default_toornament(self):
        players = [
            Cheater(),
            Detective(),
            Copycat(),
            Cooperator(),
            Grudger(),
        ]
        for pl1 in players:
            for pl2 in players:
                if pl1.name < pl2.name:
                    self.play(pl1, pl2)


class TestStringMethods(unittest.TestCase):
    def tests(self):
        print("Default toornament")
        game = Game()
        game.play()
        tops = game.top3()
        self.assertEqual(tops[0][0], 'Copycat')
        self.assertEqual(tops[1][0], 'Grudger')
        self.assertEqual(tops[2][0], 'Cheater')
        self.assertEqual(tops[0][1], 57)
        self.assertEqual(tops[1][1], 46)
        self.assertEqual(tops[2][1], 45)

    def tests_me(self):
        print()
        players = [
            Cheater(),
            Detective(),
            Copycat(),
            Cooperator(),
            Grudger(),
            Me(),
        ]
        game = Game()
        for pl1 in players:
            for pl2 in players:
                if pl1.name < pl2.name:
                    game.play(pl1, pl2)
        tops = game.top3()
        self.assertEqual(tops[0][0], 'Copycat')
        self.assertEqual(tops[1][0], 'Me')
        self.assertEqual(tops[2][0], 'Cheater')
        self.assertEqual(tops[0][1], 77)
        self.assertEqual(tops[1][1], 71)
        self.assertEqual(tops[2][1], 66)

def test_5_behaviors():
    print("TEST 5 behaviors")
    cheater = Cheater()
    cooperator = Cooperator()
    copycat = Copycat()
    grudger = Grudger()
    detective = Detective()
    g = Game()
    g.play(cheater, cooperator)
    g.play(cheater, copycat)
    g.play(cheater, grudger)
    g.play(cheater, detective)
    g.play(cooperator, copycat)
    g.play(cooperator, grudger)
    g.play(cooperator, detective)
    g.play(copycat, grudger)
    g.play(copycat, detective)
    g.play(grudger, detective)
    g.top3()
if __name__ == "__main__":
    test_5_behaviors()
    
    # unittest.main()
